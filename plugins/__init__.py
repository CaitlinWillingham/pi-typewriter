import importlib
import os

def load_plugins():
    plugin_list = []
    base = os.path.dirname(__file__)
    for file in os.listdir(base):
        if file.endswith(".py") and file != "__init__.py":
            mod_name = file[:-3]
            module = importlib.import_module(f"plugins.{mod_name}")
            plugin_list.append(module)
    return plugin_list
