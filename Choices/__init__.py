from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module
from Choices.BaseChoice import BaseChoice
from Choices.Argumentable import Argumentable
from os import getcwd
from os.path import join as join_path
from sys import argv

ARGUMENT = None

# iterate through the modules in the current package
package_dir = join_path(getcwd(), "Choices")
for (_, module_name, _) in iter_modules([package_dir]):

    # import the module and iterate through its attributes
    module = import_module(f"{__name__}.{module_name}")
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)

        if isclass(attribute):
            if issubclass(attribute, BaseChoice) and attribute != BaseChoice:
                # Add the class to this package's variables
                if not attribute.is_subcommand:
                    globals()[attribute_name] = attribute
            if issubclass(attribute, Argumentable) and attribute != Argumentable and len(argv) > 1:
                if attribute.arg == argv[1] or attribute.alias == argv[1]:
                    ARGUMENT = attribute
