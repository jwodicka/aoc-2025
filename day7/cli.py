"""
Problem definition here
"""

import click
echo = click.echo

@click.group()
def day7():
    """Solves Day 7's problems"""

@day7.command()
@click.argument("input", type=click.File("r"))
def part1(input):
    """Solves part 1"""

    lines = input.read().splitlines()
    width = len(lines[0])
    
    state = [''] * width
    echo(state)
    first_line = lines[0]
    beam_start = first_line.index('S')
    state[beam_start] = "|"
    echo(state)


    def findall(source, target):
        result = []
        index = source.find(target)
        while index > 0:
            result.append(index)
            index = source.find(target, index + 1)
        return result
    
    next_state = state
    splits = 0
    for line in lines[1:]:
        splitters = findall(line, '^')
        if splitters:
            for split in splitters:
                if state[split] == "|":
                    splits += 1
                    next_state[split-1] = "|"
                    next_state[split+1] = "|"
                    next_state[split] = ""
        state = next_state
        echo(state)

    echo(splits)


@day7.command()
@click.argument("input", type=click.File("r"))
def part2(input):
    """Solves part 2"""

    lines = input.read().splitlines()
    width = len(lines[0])
    
    state = [0] * width
    echo(state)
    first_line = lines[0]
    beam_start = first_line.index('S')
    state[beam_start] = 1
    echo(state)


    def findall(source, target):
        result = []
        index = source.find(target)
        while index > 0:
            result.append(index)
            index = source.find(target, index + 1)
        return result
    
    next_state = state
    for line in lines[1:]:
        splitters = findall(line, '^')
        if splitters:
            for split in splitters:
                if state[split] > 0:
                    next_state[split-1] = next_state[split-1] + state[split]
                    next_state[split+1] = next_state[split+1] + state[split]
                    next_state[split] = 0
        state = next_state
        echo(state)

    echo(state)
    echo(sum(state))

# When invoked as a script, do this
if __name__ == '__main__':
    day7()