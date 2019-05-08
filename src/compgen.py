"""
Pushes list of available shell stuff, e.g. built-ins, aliases, functions,
keywords, commands into stdout, runs against a separate process.
"""
import os
from constants import LIST_SHELL_COMMAND

os.system(LIST_SHELL_COMMAND)
