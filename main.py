#Imports
import os
import sys

from pip._internal.cli import cmdoptions
from pip._internal.cli.parser import (
    ConfigOptionParser,
    UpdatingDefaultsHelpFormatter,
)
from pip._internal.commands import commands_dict, get_similar_commands
from pip._internal.exceptions import CommandError
from pip._internal.utils.misc import get_pip_version, get_prog
from pip._internal.utils.typing import MYPY_CHECK_RUNNING

if MYPY_CHECK_RUNNING:
    from typing import Tuple, List


__all__ = ["create_main_parser", "parse_command"]

#Main
def main():

    parser_kw = {
        'usage': '\n%prog <command> [options]',
        'add_help_option': False,
        'formatter': UpdatingDefaultsHelpFormatter(),
        'name': 'global',
        'prog': get_prog(),
    }

    parser = ConfigOptionParser(**parser_kw)
    parser.disable_interspersed_args()

    parser.version = get_pip_version()

    # add the general options
    gen_opts = cmdoptions.make_option_group(cmdoptions.general_group, parser)
    parser.add_option_group(gen_opts)

    # so the help formatter knows
    parser.main = True  # type: ignore

    # create command listing for description
    description = [''] + [
        '{name:27} {command_info.summary}'.format(**locals())
        for name, command_info in commands_dict.items()
    ]
    parser.description = '\n'.join(description)

    return parser
