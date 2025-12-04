import click

from day1.cli import day1
from day2.cli import day2
from day3.cli import day3

@click.group()
def cli():
    """Advent of Code 2025 solutions"""

cli.add_command(day1)
cli.add_command(day2)
cli.add_command(day3)

# When invoked as a script, do this
if __name__ == '__main__':
    cli()