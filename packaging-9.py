# example_package/__init__.py
from importlib import metada
__version__ = metadata.distribution("example_package").version
del metadata # Keep top-level namespace clean
