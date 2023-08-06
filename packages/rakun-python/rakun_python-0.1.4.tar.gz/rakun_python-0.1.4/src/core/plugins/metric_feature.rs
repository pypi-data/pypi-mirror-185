use std::cell::Cell;
use std::collections::HashMap;
use pyo3::{prelude::*, types::{PyDict, PyByteArray, PyBytes}};
use pyo3::types::{PyList, PyTuple};


#[pyclass]
struct AgentMetricImpl {
    metrics: Cell<HashMap<String, Vec<f64>>>,
}

#[pymethods]
impl AgentMetricImpl {
    pub fn save(&mut self, py: Python<'_>, metric: String, value: f64) -> PyObject {
        self.metrics.get_mut().entry(metric.clone()).or_insert(vec![]).push(value);
        "ok".to_object(py)
    }

    pub fn all(&mut self) -> PyResult<Py<PyAny>> {
        let metrics_store = self.metrics.get_mut().clone();
        Python::with_gil(|py| {
            let metrics = PyDict::new(py);
            for (key, metric_values) in metrics_store.iter() {
                let values = PyList::empty(py);
                for value in metric_values {
                    values.append(value).unwrap();
                }
                metrics.set_item(key, values)?;
            }
            Ok(metrics.to_object(py))
        })
    }


    pub fn get(&mut self, name: String) -> PyResult<Py<PyAny>> {
        let metrics_store = self.metrics.get_mut().clone();
        Python::with_gil(|py| {
            let metrics = PyDict::new(py);
            for (key, metric_values) in metrics_store.iter() {
                if key == &name {
                    let values = PyList::empty(py);
                    for value in metric_values {
                        values.append(value).unwrap();
                    }
                    metrics.set_item(key, values)?;
                }
            }
            Ok(metrics.to_object(py))
        })
    }
}


#[pyclass]
pub struct AgentMetric {
    py_class: Py<PyAny>,
}

#[pymethods]
impl AgentMetric {
    #[new]
    fn __new__(wraps: Py<PyAny>) -> Self {
        AgentMetric {
            py_class: wraps,
        }
    }

    #[args(args = "*", kwargs = "**")]
    fn __call__(
        &mut self,
        py: Python<'_>,
        args: &PyTuple,
        kwargs: Option<&PyDict>,
    ) -> PyResult<Py<PyAny>> {
        let ret = self.py_class.call(py, args, kwargs)?;
        let metric = AgentMetricImpl {
            metrics: Cell::new(HashMap::new()),
        };
        ret.setattr(py, "metric", metric).unwrap();
        Ok(ret.clone_ref(py))
    }
}