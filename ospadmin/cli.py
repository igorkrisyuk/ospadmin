"""
ospadmin

Usage:
  ospadmin cluster create <name>
  ospadmin cluster update <name>
  ospadmin cluster delete <name>
  ospadmin credential get|set
  ospadmin -h | --help
  ospadmin --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  ospadmin hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/ospadmin
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import ospadmin.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(ospadmin.commands, k) and v:
            module = getattr(ospadmin.commands, k)
            ospadmin.commands = getmembers(module, isclass)
            command = [command[1] for command in ospadmin.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
