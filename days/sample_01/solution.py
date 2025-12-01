"""
Advent of Code - Sample 01 Solution (Past Year Puzzle)
"""
import sys
from pathlib import Path


def parse_input(input_data: str) -> tuple[list[int], list[int]]:
    """
    Parse the input data into two lists of numbers.
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        Tuple of two lists: (left_numbers, right_numbers)
    """
    lines = input_data.strip().split('\n')
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))
    
    return [left_list, right_list]


def solve_part_one(input_data: str) -> int:
    """
    Solve Part One of the puzzle.
    
    Find the smallest number in each list, calculate the difference,
    then do the same for the second smallest, and so on.
    Sum all the differences.
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        Solution to Part One
    """
    left_list, right_list = parse_input(input_data)
    
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate differences and sum them
    total_distance = 0
    for left, right in zip(left_sorted, right_sorted):
        total_distance += abs(left - right)
    
    return total_distance


def solve_part_two(input_data: str) -> int:
    """
    Solve Part Two of the puzzle.
    
    For each number in the left list, count how many times it appears
    in the right list, then multiply the number by its count.
    Sum all these products.
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        Solution to Part Two
    """
    left_list, right_list = parse_input(input_data)
    
    # Count occurrences of each number in the right list
    from collections import Counter
    right_counts = Counter(right_list)
    
    # For each number in left list, multiply by its count in right list
    similarity_score = 0
    for num in left_list:
        count = right_counts.get(num, 0)
        similarity_score += num * count
    
    return similarity_score


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
