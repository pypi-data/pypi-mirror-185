use pyo3::prelude::*;

#[pyfunction]
fn flatten_list_strings(list: Vec<Vec<String>>) -> PyResult<Vec<String>> {
    let result = list.into_iter().flatten().collect::<Vec<String>>();
    Ok(result)
}

/// A Python module implemented in Rust.
#[pymodule]
fn flatten_list_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(flatten_list_strings, m)?)?;
    Ok(())
}
