import setuptools
from Cython import Build

setuptools.setup(
    ext_modules=Build.cythonize("binary_module.pyx"),
)
