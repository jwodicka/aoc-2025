"""
Find invalid values in ranges

The ranges are separated by commas (,); each range gives its first ID and last ID 
separated by a dash (-).

You can find the invalid IDs by looking for any ID which is made only of some 
sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 
123123 (123 twice) would all be invalid IDs.
"""

import click
import math

echo = click.echo

@click.group()
def group():
    """Sure is a group"""

@group.command()
@click.argument("input", type=click.File("r"))
def part1(input):
    """Solves part 1"""
    # Parse input into range definitions
    ranges = parse_ranges(input)

    bad_ids = []
    # Iterate through all values in ranges
    for low, high in ranges:
        for val in range(low, high + 1):
            # Check each value for legality
                if is_illegal_id(val):
                     bad_ids.append(val)
    echo(sum(bad_ids))
                     

def parse_ranges(input):
    """
    The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).
    """
    data = input.read()
    ranges = data.split(",")
    result = []
    for range in ranges:
        low, high = range.split("-")
        result.append((int(low), int(high)))
    return result

def is_illegal_id(num):
    rep = str(num)
    length = len(rep)
    if length % 2 == 1:
        return False
    left = rep[:length//2]
    right = rep[length//2:]
    return left == right


# When invoked as a script, do this
if __name__ == '__main__':
    group()