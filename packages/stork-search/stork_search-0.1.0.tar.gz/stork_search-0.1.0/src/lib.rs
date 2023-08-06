use pyo3::prelude::*;

/// Impossibly fast web search, made for static sites
#[pymodule]
fn stork_search(_py: Python, _m: &PyModule) -> PyResult<()> {
    Ok(())
}
