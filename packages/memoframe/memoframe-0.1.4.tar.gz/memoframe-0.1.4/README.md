# 1. What is it ?

memoframe is a Python package that enables to easily optimize memory consumption of pandas dataframe. If you encounter OOM (Out of Memory) errors or slow downs during data analysis or model training.

# 2. Where to get the package ?

Binary installers for the latest released version are available at the Python Package Index (PyPI).

    # PyPI 
    pip install memoframe

# 3. Features 

- Optimize integer memory usage
- Optimize float memory usage
- Optimize object memory usage
- Get an estimation of the memory usage saved

# 4. How to use the library

    from memoframe import memoframe as mf
    
    # dataframe is a pandas DataFram
    optimized_dataframe = mf.downsize_memory(dataframe)

    # Estimates memory usage gains
    mf.get_opti_info(dataframe)
