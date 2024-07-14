import os
import traceback
from importlib import util


class PluginHandler:
    """Basic resource class. Concrete resources will inherit from this one
    """
    plugins = {}

    # For every class that inherits from the current,
    # the class name will be added to plugins
    def __init_subclass__(cls, **kwargs):
        #print("__init_subclass__", cls, "----", cls.__class__)
        super().__init_subclass__(**kwargs)
        inst = cls()
        #print("NAME: ",type(inst).__name__)
        cls.plugins[type(inst).__name__] = inst


# Small utility to automatically load modules
def load_module(path):
    #print("load_module, pth: ", path)
    name = os.path.split(path)[-1]
    #print("name: ", name)
    spec = util.spec_from_file_location(name, path)
    #print("spc: ", spec)
    module = util.module_from_spec(spec)
    #print("module: ", module)
    spec.loader.exec_module(module)
    return module


# Get current path
path = os.path.abspath(__file__)
dirpath = os.path.dirname(path)

for fname in os.listdir(dirpath):
    # Load only "real modules"
    #print("for loop")
    if not fname.startswith('.') and \
       not fname.startswith('__') and fname.endswith('.py'):
        try:
            #print("for loop", dirpath, fname)
            load_module(os.path.join(dirpath, fname))
        except Exception:
            traceback.print_exc()
