use std::time::SystemTime;
use pyo3::prelude::*;
use pyo3::types::{PyDict, PyTuple};

fn get_code(name: &str) -> String {
    let uuid = SystemTime::now()
        .duration_since(SystemTime::UNIX_EPOCH)
        .unwrap()
        .as_nanos();
    format!("AG-{}-{}", name, uuid)
}

#[pyclass]
pub struct Agent {
    py_class: Py<PyAny>,
}

#[pymethods]
impl Agent {
    #[new]
    fn __new__(wraps: Py<PyAny>) -> Self {
        Agent {
            py_class: wraps
        }
    }

    #[args(args = "*", kwargs = "**")]
    fn __call__(
        &mut self,
        py: Python<'_>,
        args: &PyTuple,
        kwargs: Option<&PyDict>,
    ) -> PyResult<Py<PyAny>> {
        let name = self.py_class.getattr(py, "__name__")?;
        let ret = self.py_class.call(py, args, kwargs)?;
        let code = get_code(name.to_string().as_str()); // Get Unique Code
        ret.setattr(py, "code", code.clone())?;
        Ok(ret.clone_ref(py))
    }
}
