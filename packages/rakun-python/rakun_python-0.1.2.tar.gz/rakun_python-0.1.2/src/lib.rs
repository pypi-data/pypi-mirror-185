mod core;

use pyo3::prelude::*;
use crate::core::agent::Agent;
use crate::core::manager::AgentManager;


/// A Python module implemented in Rust.
#[pymodule]
fn rakun_python(_py: Python, m: &PyModule) -> PyResult<()> {
    // m.add_function(wrap_pyfunction!(start_comm_server, m)?)?;
    // m.add_function(wrap_pyfunction!(create_agent, m)?)?;
    m.add_class::<Agent>()?;
    m.add_class::<AgentManager>()?;
    Ok(())
}