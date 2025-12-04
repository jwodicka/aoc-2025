"""
Problem definition here
"""

import click
echo = click.echo

@click.group()
def dayN():
    """Solves Day N's problems"""

@dayN.command()
@click.argument("input", type=click.File("r"))
def part1(input):
    """Solves part 1"""

@dayN.command()
@click.argument("input", type=click.File("r"))
def part2(input):
    """Solves part 2"""

# When invoked as a script, do this
if __name__ == '__main__':
    dayN()