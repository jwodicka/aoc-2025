"""
Problem definition here
"""

import re
import click
from queue import SimpleQueue, PriorityQueue
from collections import Counter
from itertools import product
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

    power = tuple(map(int, power_str.split(",")))

    return (lights, buttons, power)

def find_fewest_buttons(target, buttons):
    queue = SimpleQueue()
    width = len(target)
    intial_state = (False,)*width
    best_depth = {}
    best_depth[intial_state] = 0

    queue.put(intial_state)

    while not queue.empty():
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

def is_overshot(target, state):
    for s_val, t_val in zip(state, target):
        if s_val > t_val:
            return True
    return False

def find_fewest_increments(target, buttons):
    """
    This works! But we might be here a while...
    """
    queue = SimpleQueue()
    width = len(target)
    intial_state = (0,)*width
    best_depth = {}
    best_depth[intial_state] = 0

    queue.put(intial_state)

    while not queue.empty():
        state = queue.get()
        # echo(state)
        depth = best_depth[state]
        for button in buttons:
            tmp = list(state)
            for position in button:
                tmp[position] += 1
            new_state = tuple(tmp)
            if is_overshot(target, new_state):
                continue
            if new_state not in best_depth:
                best_depth[new_state] = depth + 1
                queue.put(new_state)
                if new_state == target:
                    return best_depth[new_state]
    return -1

def apply_button(button, state):
    tmp = list(state)
    for position in button:
        tmp[position] += 1
    return tuple(tmp)

def find_fewest_increments_greedy(target, buttons):
    """
    Is it fast? Yep!
    Is it correct? ... ... ... well, that might be a problem.
    """
    queue = SimpleQueue()
    width = len(target)
    intial_state = (0,)*width
    best_depth = {}
    best_depth[intial_state] = 0

    queue.put(intial_state)

    counts = Counter([n for button in buttons for n in button])
    echo(counts)


    while not queue.empty():
        state = queue.get()
        # echo(state)
        depth = best_depth[state]
        for button in buttons:
            new_state = state
            next_state = apply_button(button, new_state)
            presses = 0
            while not is_overshot(target, next_state):
                new_state = next_state
                next_state = apply_button(button, new_state)
                presses += 1
            if presses == 0:
                continue
            if new_state not in best_depth or best_depth[new_state] > depth + presses:
                best_depth[new_state] = depth + presses
                
                queue.put(new_state)
                if new_state == target:
                    return best_depth[new_state]
    return -1

def most_constrained_position(target, buttons):
    counts = Counter([n for button in buttons for n in button])

    min_count = min(counts.values())

    constrained_positions = [key for key in counts.keys() if counts[key] == min_count]

    # If there are multiple constrained positions, sort ascending by target size.
    if len(constrained_positions) > 1:
        constrained_positions.sort(key=lambda n : target[n])

    return constrained_positions[0]

def find_fewest_increments_v2(target, buttons):
    """
    New approach:

    Choose the most constrained digit (fewest buttons, break ties by lowest value)
    If there is only one button that can adjust that digit, press that many times.
        Remove that button from consideration
    If there are multiple buttons that can adjust that digit,
        Find all combinations - e.g., if there are two buttons and the digit needs 5:
        0/5, 1/4, 2/3, 3/2, 4/1, 5/0
        Fan out for all of these :( 
        In fanout, remove all buttons that touch this digit from consideration.

    Repeat this process to keep eliminating digits.
    """

    queue = SimpleQueue()
    width = len(target)
    intial_state = (0,)*width
    best_depth = {}
    best_depth[intial_state] = 0

    queue.put(intial_state)

    target_pos = most_constrained_position(target, buttons)
    echo(target_pos)

    valid_buttons = list(filter(lambda b : target_pos in b, buttons))
    echo(valid_buttons)
    target_val = target[target_pos]
    echo(target_val)
    splits = build_splits(len(valid_buttons), target_val)
    echo(len(splits))
    
def build_splits(ways, n):
    if ways == 1:
        return [(n,)]
    if n == 0:
        return [(0,)*ways]
    return [(x, *split) for x in range(n) for split in build_splits(ways - 1, n-x)]


def a_star(target, buttons):
    """
    Probably correct, but still too slow.
    """
    # A* Planning
    # Cost is total number of presses to get to this point
    # h = (sum(target) - sum(state)) / size(biggest button)
    queue = PriorityQueue()
    
    width = len(target)
    intial_state = (0,)*width

    target_sum = sum(target)
    best_button = max(map(len, buttons))

    def h(state):
        return (target_sum - sum(state)) / best_button

    best_depth = {}
    best_depth[intial_state] = 0
    
    estimated_depth = {}

    def enqueue(state):
        estimated_depth[state] = best_depth[state] + h(state)
        queue.put((estimated_depth[state], state))
    
    def dequeue():
        _, state = queue.get()
        return state
    
    enqueue(intial_state)

    while not queue.empty():
        state = dequeue()
        # echo(state)
        depth = best_depth[state]
        for button in buttons:
            tmp = list(state)
            for position in button:
                tmp[position] += 1
            new_state = tuple(tmp)
            if is_overshot(target, new_state):
                continue
            if new_state not in best_depth:
                best_depth[new_state] = depth + 1
                enqueue(new_state)
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

    lines = input.read().splitlines()

    machines = list(map(parse_machine, lines))
    
    result = 0
    # for _, buttons, target in machines:
    #     echo(target)
    #     best = a_star(target, buttons)
    #     echo(best)
    #     result += best
    _, buttons, target = machines[3]
    result = find_fewest_increments_v2(target, buttons)

    # echo(result)
    # echo(build_splits(1, 5))

    # echo(build_splits(4, 5))

# When invoked as a script, do this
if __name__ == '__main__':
    day10()