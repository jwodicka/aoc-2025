"""
Problem definition here
"""

import re
import functools
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

    lines = input.read().splitlines()
    columns = list(zip(*lines, strict=True))

    def strip_space(tuple):
        return list(filter(lambda item : item != " ", tuple))

    stripped = list(map(strip_space, columns))

    problems = []
    current_problem = []
    current_operator = ""
    for column in stripped:
        match column:
            case [*digits, "*"]:
                current_operator = "*"
                current_problem.append(int("".join(digits)))
            case [*digits, "+"]:
                current_operator = "+"
                current_problem.append(int("".join(digits)))
            case []:
                problems.append((current_operator, current_problem))
                current_problem = []
                current_operator = ""
            case [*digits]:
                current_problem.append(int("".join(digits)))
            case _:
                echo(column)
                raise ValueError("That's not math!")
    problems.append((current_operator, current_problem))

    echo(problems)

    def mult(a, b):
        return a * b

    def solve(problem):
        match problem:
            case ('*', digits):
                return functools.reduce(mult, digits)
            case ('+', digits):
                return sum(digits)
            case _:
                echo(problem)
                raise ValueError("That's not math!")
            
    solutions = list(map(solve, problems))

    echo(solutions)

    echo(sum(solutions))
        


# When invoked as a script, do this
if __name__ == '__main__':
    day6()