"""
Advent of Code - Sample 02 Solution (Past Year Puzzle)
"""
import sys
import re
from pathlib import Path


def parse_input(input_data: str) -> list:
    """
    Parse the input data to extract valid mul(x,y) patterns.
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        List of tuples containing (x, y) pairs from valid mul(x,y) patterns
    """
    # Use regex to find all valid mul(x,y) patterns
    # Pattern: mul( followed by digits, comma, digits, closing )
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, input_data)
    
    # Convert string tuples to integer tuples
    return [(int(x), int(y)) for x, y in matches]


def solve_part_one(input_data: str) -> int:
    """
    Solve Part One of the puzzle.
    
    Find all valid mul(x,y) patterns in the input string,
    multiply each pair, and return the sum of all products.
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        Sum of all products from valid mul(x,y) patterns
    """
    mul_pairs = parse_input(input_data)
    
    # Calculate the sum of all products
    total = sum(x * y for x, y in mul_pairs)
    
    return total


def solve_part_two(input_data: str) -> int:
    """
    Solve Part Two of the puzzle.
    
    Same as Part One, but mul(x,y) operations are only processed when enabled.
    - Start in enabled state
    - When encountering don't(), disable processing until next do()
    - When encountering do(), re-enable processing
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        Sum of all products from enabled mul(x,y) patterns
    """
    # Pattern to match mul(x,y), do(), or don't()
    # Use groups to capture the numbers in mul()
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    
    enabled = True  # Start in enabled state
    total = 0
    
    # Find all matches in order (left to right)
    for match in re.finditer(pattern, input_data):
        matched_text = match.group(0)
        
        if matched_text == "don't()":
            enabled = False
        elif matched_text == "do()":
            enabled = True
        elif matched_text.startswith("mul(") and enabled:
            # Extract the numbers from the captured groups
            x, y = int(match.group(1)), int(match.group(2))
            total += x * y
    
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
