use pyo3::{prelude::*, PyResult, Python};
use pyo3::types::PyDict;

#[derive(Clone, Debug)]
pub struct Message {
    pub sender: String,
    pub from: String,
    pub data: Py<PyAny>,
    pub receiver: Option<String>,
}

#[derive(Clone, Debug)]
#[pyclass]
pub struct PyMessage {
    #[pyo3(get, set)]
    pub sender: String,
    #[pyo3(get, set)]
    pub from: String,
    #[pyo3(get, set)]
    pub data: Py<PyAny>,
    #[pyo3(get, set)]
    pub receiver: Option<String>,
}

impl From<Message> for PyMessage {
    fn from(message: Message) -> Self {
        PyMessage {
            sender: message.sender,
            from: message.from,
            data: message.data,
            receiver: message.receiver,
        }
    }
}

impl Message {
    pub fn get_py_message(&self, py: Python) -> PyMessage {
        PyMessage::from(self.clone())
    }
}