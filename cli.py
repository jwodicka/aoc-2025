import click

from day1.cli import day1
from day2.cli import day2
from day3.cli import day3
from day4.cli import day4
from day5.cli import day5
from day6.cli import day6
from day7.cli import day7
from day8.cli import day8
from day9.cli import day9
from day10.cli import day10

@click.group()
def cli():
    """Advent of Code 2025 solutions"""

cli.add_command(day1)
cli.add_command(day2)
cli.add_command(day3)
cli.add_command(day4)
cli.add_command(day5)
cli.add_command(day6)
cli.add_command(day7)
cli.add_command(day8)
cli.add_command(day9)
cli.add_command(day10)

# When invoked as a script, do this
if __name__ == '__main__':
    cli()