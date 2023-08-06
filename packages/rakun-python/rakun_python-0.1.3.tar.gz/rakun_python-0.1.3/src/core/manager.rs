use std::cell::Cell;
use pyo3::prelude::*;
use std::collections::HashMap;
use std::fmt::{Display, Formatter};
use std::sync::{Arc, mpsc, Mutex};
use std::sync::mpsc::{
    SyncSender,
    Receiver,
};
use pyo3::{Py, PyAny, pyclass};
use pyo3::exceptions::PyOSError;
use pyo3::types::PyString;
use crate::core::core::AgentCore;
use crate::core::data::Message;


#[derive(Debug)]
struct AgentAlreadyExistsError;

impl Display for AgentAlreadyExistsError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "Agent Domain name already exists")
    }
}

impl std::convert::From<AgentAlreadyExistsError> for PyErr {
    fn from(err: AgentAlreadyExistsError) -> PyErr {
        PyOSError::new_err(err.to_string())
    }
}

impl std::error::Error for AgentAlreadyExistsError {}


#[pyclass]
pub struct AgentManager {
    pub agents: HashMap<String, Arc<Py<PyAny>>>,
    pub observer: Arc<Mutex<Receiver<Message>>>,
    pub publisher: Arc<Mutex<SyncSender<Message>>>,
}

fn validate_name_exists(name: &str, agents: &HashMap<String, Arc<Py<PyAny>>>) -> bool {
    agents.contains_key(name)
}

#[pymethods]
impl AgentManager {
    #[new]
    pub fn _new() -> Self {
        let (publisher, observer): (SyncSender<Message>, Receiver<Message>) = mpsc::sync_channel(1);
        Self {
            agents: HashMap::new(),
            observer: Arc::new(Mutex::new(observer)),
            publisher: Arc::new(Mutex::new(publisher)),
        }
    }

    fn register(&mut self, agent: Py<PyAny>, domain_name: String) -> Result<(), AgentAlreadyExistsError> {
        if validate_name_exists(domain_name.as_str(), &self.agents) {
            return Err(AgentAlreadyExistsError);
        }
        let publisher = Arc::clone(&self.publisher);
        Python::with_gil(|py| {
            let agent_ref = agent.call(py, (), None).unwrap();
            let code = agent_ref.getattr(py, "code").unwrap();
            let code = code.to_string();
            let core = AgentCore {
                agent_id: Arc::new(code.to_string()),
                domain_name: Arc::new(domain_name.to_string()),
                publisher: publisher.clone(),
            };
            agent_ref.setattr(py, "core", core).unwrap();
            agent_ref.setattr(py, "domain_name", domain_name.clone()).unwrap();
            self.agents.insert(domain_name, Arc::new(agent_ref.clone_ref(py)));
        });
        Ok(())
    }

    fn start<'a>(&'a self, py: Python<'a>) -> PyResult<&'a PyAny> {
        let mut agents_rx = vec![];

        let agents = self.agents.clone();

        for (key, agent) in agents.clone().iter() {
            let agent = Arc::clone(agent);
            println!("Starting agent: {} {}", key, agent);
            let res = async_std::task::spawn(async move {
                Python::with_gil(|py| {
                    let asyncio = py.import("asyncio").unwrap();
                    let event_loop = asyncio.call_method0("new_event_loop").unwrap();
                    asyncio.call_method1("set_event_loop", (event_loop, )).unwrap();
                    let event_loop_hdl = PyObject::from(event_loop);
                    let agent = agent.as_ref().as_ref(py);
                    let method_run = agent.call_method0("run").unwrap();
                    event_loop_hdl.as_ref(py).call_method1("run_until_complete", (method_run, )).unwrap();
                });
            });
            agents_rx.push(res);
        }

        let incoming = Arc::clone(&self.observer);
        let rx2 = async_std::task::spawn(async move {
            let rx = incoming.lock().unwrap();
            while let message = rx.recv().unwrap() {
                for (agent_domain_name, agent) in agents.clone().iter() {
                    if let Some(receiver) = &message.receiver {
                        if receiver == &"system".to_string() {
                            let data = message.data.clone();
                            if data.to_string() == "shutdown".to_string() {
                                println!("Shutting down");
                                std::process::exit(0);
                            }
                        }
                        if agent_domain_name != receiver {
                            continue;
                        }
                    }
                    let message = message.clone();
                    let agent = Arc::clone(agent);
                    async_std::task::spawn(async move {
                        Python::with_gil(|py| {
                            let asyncio = py.import("asyncio").unwrap();
                            let event_loop = asyncio.call_method0("new_event_loop").unwrap();
                            asyncio.call_method1("set_event_loop", (event_loop, )).unwrap();
                            let event_loop_hdl = PyObject::from(event_loop);
                            let agent = agent.as_ref().as_ref(py);
                            let method_run = agent.call_method1("receiver", (message.sender.clone(), message.get_py_message(py), )).unwrap();
                            event_loop_hdl.as_ref(py).call_method1("run_until_complete", (method_run, )).unwrap();
                        });
                    });
                }
            }
        });

        pyo3_asyncio::async_std::future_into_py(py, async move {
            for agent in agents_rx {
                agent.await;
            }
            rx2.await;
            Ok(Python::with_gil(|py| "ok".to_object(py)))
        })
    }
}