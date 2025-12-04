"""
Advent of Code 2025 - Day 02 Solution
"""
import sys
from pathlib import Path


def parse_input(input_data: str) -> list:
    """Parse comma-separated ranges into list of (start, end) tuples."""
    if not input_data.strip():
        return []
    
    ranges = []
    for range_str in input_data.strip().split(','):
        start, end = range_str.strip().split('-')
        ranges.append((int(start), int(end)))
    
    return ranges


def has_repeating_pattern(num: int) -> bool:
    """Check if a number has a pattern that repeats exactly twice."""
    s = str(num)
    length = len(s)
    
    if length % 2 != 0:
        return False
    
    pattern_len = length // 2
    pattern = s[:pattern_len]
    return pattern * 2 == s


def solve_part_one(input_data: str) -> int:
    """Find sum of all numbers with repeating patterns in given ranges."""
    ranges = parse_input(input_data)
    total = 0
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if has_repeating_pattern(num):
                total += num
    
    return total


def has_repeating_pattern_at_least_twice(num: int) -> bool:
    """Check if a number has a pattern that repeats 2 or more times."""
    s = str(num)
    length = len(s)
    
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            repetitions = length // pattern_len
            if repetitions >= 2:
                pattern = s[:pattern_len]
                if pattern * repetitions == s:
                    return True
    
    return False


def solve_part_two(input_data: str) -> int:
    """Find sum of all numbers with patterns repeated 2+ times."""
    ranges = parse_input(input_data)
    total = 0
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if has_repeating_pattern_at_least_twice(num):
                total += num
    
    return total


if __name__ == "__main__":
    # Get input file from command line or use default
    if len(sys.argv) > 1:
        input_file = Path(sys.argv[1])
    else:
        input_file = Path(__file__).parent / "input.txt"
    
    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    puzzle_input = input_file.read_text()
    
    print(f"Part One: {solve_part_one(puzzle_input)}")
    print(f"Part Two: {solve_part_two(puzzle_input)}")
