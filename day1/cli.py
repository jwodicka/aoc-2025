"""
The attached document (your puzzle input) contains a sequence of rotations, one 
per line, which tell you how to open the safe.A rotation starts with an L or R 
which indicates whether the rotation should be to the left (toward lower numbers)
or to the right (toward higher numbers). Then, the rotation has a distance value
which indicates how many clicks the dial should be rotated in that direction.

Because the dial is a circle, turning the dial left from 0 one click makes it 
point at 99. Similarly, turning the dial right from 99 one click makes it point
at 0.

The dial starts by pointing at 50.

You could follow the instructions, but your recent required official North Pole
secret entrance security training seminar taught you that the safe is actually a
decoy. The actual password is the number of times the dial is left pointing at 0
after any rotation in the sequence.
"""

import click
import math

echo = click.echo

@click.group()
def day1():
    """Solves Day 1's problems"""

@day1.command()
@click.argument("input", type=click.File("r"))
def part1(input):
    """Solves part 1"""
    values = parse_dial(input)
    
    # The dial starts at 50, per instructions
    dial = 50
    zeroes = 0
    for value in values:
        dial += value
        dial %= 100
        if dial == 0:
            zeroes += 1

    echo(zeroes)
    

@day1.command()
@click.argument("input", type=click.File("r"))
def part2(input):
    """Solves part 2"""
    values = parse_dial(input)

    # The dial starts at 50, per instructions
    dial = 50
    zeroes = 0
    for value in values:
        # If abs(value) > 100, figure out how many full spins need removing.
        # Convert to a number between -99 + 99
        abs_val = abs(value)
        spins = 0
        val = value
        if abs_val >= 100:
            spins = abs_val // 100
            abs_val %= 100
            val = int(math.copysign(abs_val, value))
            assert(abs(val) == abs_val)

        # Don't double-count zeroes you counted already!
        if dial == 0 and val < 0:
            echo("Double-count avoidance")
            spins -= 1
        dial = dial + val
        if dial != dial % 100:
            echo("Spun past!")
            spins += 1
        if dial == 100:
            echo("Right double-count avoidance")
            spins -= 1
        dial %= 100
        if dial == 0:
            echo("Hit Zero!")
            zeroes += 1

        zeroes += spins
        echo('v{0} s{1} z{2} d{3}'.format(value, spins, zeroes, dial))
    echo(zeroes)

def parse_dial(input):
    values = []
    # Read the input file into values, making L numbers negative and R positive
    for line in input.read().splitlines():
        value = int(line[1:])
        if str(line[0]) == 'L':
            value = value * -1
        values.append(value)
    return values


# This is modular math!

# Load an input file
# Parse the input file

# Simulate the turns
# Record 0s

# Print the number of 0s


# When invoked as a script, do this
if __name__ == '__main__':
    day1()