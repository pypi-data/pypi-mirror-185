```rust

struct AgentHelper {
    agent: PyObject,
    incoming: Receiver<Message>,
    outgoing: Sender<Message>,
    // server: RefCell<Server>,
    // server: Server,
}

#[derive(Debug)]
enum AgentHelperError {
    PyError(PyErr),
    TokioError(tokio::task::JoinError),
}


impl AgentHelper {
    fn new(py: Python<'_>, agent: &PyAny, incoming: Receiver<Message>, outgoing: Sender<Message>) -> PyResult<Self> {
        let agent_obj = agent.to_object(py);
        let messenger = outgoing.clone();
        let message_fn = pyo3_asyncio::tokio::future_into_py(py, async move {
            messenger.send(Message {
                from: "python".to_string(),
                data: "hello".to_string(),
            }).await;
            Ok(())
        }).unwrap();
        let message_fn = Py::from(message_fn);
        agent.setattr("message", message_fn).unwrap();


        Ok(Self {
            agent: agent_obj,
            incoming,
            outgoing: outgoing.clone(),
            // server,
            // server: RefCell::new(server),
        })
    }

    // fn run<'p>(&mut self, py: Python<'p>) -> PyResult<&'p PyAny> {
    //     // let start_fn = async move {
    //     //     let server = &mut self.server;
    //     //     server.start().await;
    //     // };\
    //     let server = self.server.get_mut();
    //     let res = pyo3_asyncio::tokio::future_into_py(py, async move {
    //         server.start().await;
    //         Ok(())
    //     });
    //
    //     res
    // }

    fn run<'p>(&self, py: Python<'p>) -> PyResult<&'p PyAny> {
        let agent = self.agent.as_ref(py);
        let method_run = agent.call_method0("run").unwrap();
        let run = pyo3_asyncio::tokio::into_future(method_run).unwrap();
        pyo3_asyncio::tokio::future_into_py(py, async move {
            let result = match run.await {
                Ok(result) => result,
                Err(e) => {
                    println!("Error: {}", e);
                    return Ok(());
                }
            };
            Ok(())
        })
    }
}

/// Formats the sum of two numbers as string.
#[pyfunction]
fn manage<'a>(py: Python<'a>, agent: &'a PyAny) -> PyResult<&'a PyAny> {
    let (outgoing, mut incoming) = mpsc::channel(10);
    let (mut server, messenger) = Server::new(outgoing);


    let mut agent_helper = match AgentHelper::new(py, agent, incoming, messenger) {
        Ok(agent_helper) => agent_helper,
        Err(e) => {
            println!("Error: {:?}", e);
            return Err(PyErr::from(e));
        }
    };

    agent_helper.run(py);


    pyo3_asyncio::tokio::future_into_py(py, async move {
        // inner.await;
        server.start().await;
        Ok(())
    })
}

/// Formats the sum of two numbers as string.
#[pyfunction]
fn start_comm_server(py: Python, dial_up: Option<String>) -> PyResult<&PyAny> {
    pyo3_asyncio::tokio::future_into_py(py, async move {
        let _ = rakun_libs::server(dial_up).await;
        Ok(())
    })
}

```