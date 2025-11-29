"""
Advent of Code - Sample 03 Solution (Past Year Puzzle)
"""
import sys
from pathlib import Path


def parse_input(input_data: str) -> list:
    """
    Parse the input data.
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        Parsed data structure
    """
    lines = input_data.strip().split('\n')
    return lines


def solve_part_one(input_data: str) -> int:
    """
    Solve Part One of the puzzle.
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        Solution to Part One
    """
    data = parse_input(input_data)
    # TODO: Implement solution for Part One
    raise NotImplementedError("Part One solution not yet implemented")


def solve_part_two(input_data: str) -> int:
    """
    Solve Part Two of the puzzle.
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        Solution to Part Two
    """
    data = parse_input(input_data)
    # TODO: Implement solution for Part Two
    raise NotImplementedError("Part Two solution not yet implemented")


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
