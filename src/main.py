import os
import subprocess
from constants import (BASH_HISTORYFILE_PATH, OUTPUT_MESSAGE)


def get_last_history_event():
    """
    :return: last user's input before 'crap', which is
    pre-last bash history element (the last is always '')
    """
    with open(os.path.expanduser(BASH_HISTORYFILE_PATH)) as f:
        last_event = f.read().split('\n')[-2]
    return last_event


def get_all_available_stuff_from_shell():
    """
    Runs process compgen.py, connects with it and
    reads all available built-ins, aliases, functions, keywords, commands
    from stdout of compgen.py process
    :return: list of all available bash stuff
    """
    proc = subprocess.Popen(
        ['python', os.path.expanduser('crap/src/compgen.py')],
        stdout=subprocess.PIPE
    )
    commands = list()
    while True:
        line = proc.stdout.readline()
        if line != '':
            commands.append(line.rstrip())
        else:
            break
    return commands


def get_all_possible_matches(last_user_input, all_shell_stuff):
    """
    :param last_user_input:
    :param all_shell_stuff:
    :return: list of possible shell commands according to last user's input
    """
    possible_matches = list()
    for possible_command in all_shell_stuff:
        if last_user_input[0] == possible_command[0]:
            possible_matches.append(possible_command)
    return possible_matches


def format_out(last_user_input, all_shell_stuff):
    """
    :param last_user_input:
    :param all_shell_stuff:
    :return: string that more readable than python lists __str__()
    """
    formatted_commands = ''
    for entry in get_all_possible_matches(last_user_input, all_shell_stuff):
        formatted_commands = formatted_commands + ' ' + entry
    return formatted_commands.lstrip()


last_user_input = get_last_history_event()
available_commands = get_all_available_stuff_from_shell()
out_commands = format_out(last_user_input, available_commands)

print OUTPUT_MESSAGE % out_commands
