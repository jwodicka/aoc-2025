"""
Problem definition here
"""

import re
import click
echo = click.echo

@click.group()
def day6():
    """Solves Day 6's problems"""

@day6.command()
@click.argument("input", type=click.File("r"))
def part1(input):
    """Solves part 1"""

    lines = input.read().splitlines()
    lists = map(lambda line : list((item for item in re.split(r' +', line) if len(item) > 0)), lines)
    problems = list(zip(*lists, strict=True))

    def solve(problem):
        match problem:
            case (a, b, c, '*'):
                return int(a) * int(b) * int(c)
            case (a, b, c, d, '*'):
                return int(a) * int(b) * int(c) * int(d)
            case (a, b, c, '+'):
                return int(a) + int(b) + int(c)
            case (a, b, c, d, '+'):
                return int(a) + int(b) + int(c) + int(d)
            case _:
                echo(problem)
                raise ValueError("That's not math!")
            
    solutions = list(map(solve, problems))
    echo(solutions)

    echo(sum(solutions))


@day6.command()
@click.argument("input", type=click.File("r"))
def part2(input):
    """Solves part 2"""

# When invoked as a script, do this
if __name__ == '__main__':
    day6()