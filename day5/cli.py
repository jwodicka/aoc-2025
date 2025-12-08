"""
Problem definition here
"""

import click
echo = click.echo

@click.group()
def day5():
    """Solves Day 5's problems"""

@day5.command()
@click.argument("input", type=click.File("r"))
def part1(input):
    """Solves part 1"""

    ranges_s, items_s = input.read().split("\n\n")
    ranges_list = ranges_s.split("\n")
    ranges_pairs = list(map(lambda s : s.split("-"), ranges_list))
    ranges = list(map(lambda pair: (int(pair[0]), int(pair[1])), ranges_pairs))
    
    items = list((int(item) for item in items_s.split("\n") if len(item) > 0))
    echo(ranges)
    echo(items)

    def is_in_range(item, range):
        low, high = range
        return item >= low and item <= high
    
    fresh = []
    for item in items:
        if any(map(lambda range : is_in_range(item, range), ranges)):
            fresh.append(item)
    
    echo(fresh)
    echo(len(fresh))

@day5.command()
@click.argument("input", type=click.File("r"))
def part2(input):
    """Solves part 2"""

    ranges_s, _ = input.read().split("\n\n")
    ranges_list = ranges_s.split("\n")
    ranges_pairs = list(map(lambda s : s.split("-"), ranges_list))
    ranges = list(map(lambda pair: (int(pair[0]), int(pair[1])), ranges_pairs))

    # echo(ranges)

    sorted_ranges = sorted(ranges, key=lambda r : r[0])
    
    echo("SORTED")
    echo(sorted_ranges)

    merged_ranges = []
    prev_low = sorted_ranges[0][0]
    prev_high = sorted_ranges[0][1]
    for low, high in sorted_ranges:
        if low <= prev_high:
            if high > prev_high:
                prev_high = high
        else:
            merged_ranges.append((prev_low, prev_high))
            prev_low = low
            prev_high = high
    merged_ranges.append((prev_low, prev_high))

    echo("MERGED")
    echo(merged_ranges)

    range_sizes = list(map(lambda range : range[1] - range[0] + 1, merged_ranges))

    echo(range_sizes)

    echo(sum(range_sizes))



# When invoked as a script, do this
if __name__ == '__main__':
    day5()