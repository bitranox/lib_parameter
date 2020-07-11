# EXT
from click.testing import CliRunner

# OWN
import lib_parameter.lib_parameter_cli as lib_parameter_cli

runner = CliRunner()
runner.invoke(lib_parameter_cli.cli_main, ['--version'])
runner.invoke(lib_parameter_cli.cli_main, ['-h'])
runner.invoke(lib_parameter_cli.cli_main, ['info'])
