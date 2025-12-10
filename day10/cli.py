"""
Problem definition here
"""

import re
import click
from queue import Queue
echo = click.echo

@click.group()
def day10():
    """Solves Day 10's problems"""

def parse_machine(line):
    matches = re.match(r"\[([#\.]+)\]((?: \([\d,]+\))+) \{([\d,]+)\}", line)
    if matches:
        light_str, button_str, power_str = matches.groups()
    lights = tuple(map(lambda c : c == "#", light_str))

    def parse_button(str):
        return list(map(int, str[1:-1].split(",")))
    
    buttons = list(map(parse_button, button_str.split()))

    power = list(map(int, power_str.split(",")))

    return (lights, buttons, power)

def find_fewest_buttons(target, buttons):
    queue = Queue()
    width = len(target)
    intial_state = (False,)*width
    best_depth = {}
    best_depth[intial_state] = 0

    queue.put(intial_state)

    while queue.not_empty:
        state = queue.get()
        depth = best_depth[state]
        for button in buttons:
            tmp = list(state)
            for position in button:
                tmp[position] = not tmp[position]
            new_state = tuple(tmp)
            if new_state not in best_depth:
                best_depth[new_state] = depth + 1
                queue.put(new_state)
                if new_state == target:
                    return best_depth[new_state]
    return -1

@day10.command()
@click.argument("input", type=click.File("r"))
def part1(input):
    """Solves part 1"""

    lines = input.read().splitlines()

    machines = list(map(parse_machine, lines))
    
    result = 0
    for target, buttons, _ in machines:
        best = find_fewest_buttons(target, buttons)
        result += best

    echo(result)

@day10.command()
@click.argument("input", type=click.File("r"))
def part2(input):
    """Solves part 2"""

# When invoked as a script, do this
if __name__ == '__main__':
    day10()