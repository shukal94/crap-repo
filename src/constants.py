"""
Constants, paths, commands are stored here
"""


OUTPUT_MESSAGE = 'Did you mean:\n%s ?'

BASH_HISTORYFILE_PATH = '~/.bash_history'

# covers aliases, functions, keywords, commands
# that are available on your shell
LIST_SHELL_COMMAND = 'compgen -A function -abck'
