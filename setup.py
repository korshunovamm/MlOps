from setuptools import setup, find_packages
from glob import glob

so_files = glob("chebyshevDistance/python/trace_core*.so")

setup(
    name="chebyshevDistance",
    version="0.1",
    description="Chebyshev Distance of two vectors with Python bindings",
    packages=find_packages(),
    package_data={
        "chebyshevDistance": ["python/*.so"],
    },
)