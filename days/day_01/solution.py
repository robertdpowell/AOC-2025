"""
Advent of Code 2025 - Day 01 Solution
"""
import sys
from pathlib import Path


def parse_input(input_data: str) -> list:
    """
    Parse the input data into list of (direction, amount) tuples.
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        List of tuples: (direction, amount) where direction is 'L' or 'R'
    """
    if not input_data.strip():
        return []
    
    lines = input_data.strip().split('\n')
    instructions = []
    
    for line in lines:
        line = line.strip()
        if line:
            direction = line[0]  # First character is L or R
            amount = int(line[1:])  # Rest is the number
            instructions.append((direction, amount))
    
    return instructions


def solve_part_one(input_data: str) -> int:
    """
    Solve Part One of the puzzle.
    
    Starting at position 50 on a circular dial (0-99), count how many 
    times the position stops at 0 after a move. The dial wraps around
    using modulo 100.
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        Count of times position lands exactly on 0
    """
    instructions = parse_input(input_data)
    
    position = 50  # Starting position on circular dial (0-99)
    zero_count = 0
    
    for direction, amount in instructions:
        # Update position based on direction
        if direction == 'L':
            position -= amount
        else:  # direction == 'R'
            position += amount
        
        # Wrap around using modulo 100 (circular dial 0-99)
        position = position % 100
        
        # Count only when we land exactly on 0
        if position == 0:
            zero_count += 1
    
    return zero_count


def solve_part_two(input_data: str) -> int:
    """
    Solve Part Two of the puzzle.
    
    Count both stops at 0 AND crossings over 0 during dial movement.
    A crossing occurs when movement wraps around the dial passing through 0.
    
    Args:
        input_data: Raw input string from the puzzle
        
    Returns:
        Total count of stops and crossings at 0
    """
    instructions = parse_input(input_data)
    
    position = 50  # Starting position on circular dial (0-99)
    count = 0
    
    for direction, amount in instructions:
        old_position = position
        
        # Calculate new position
        if direction == 'L':
            position = (position - amount) % 100
        else:  # direction == 'R'
            position = (position + amount) % 100
        
        # Count how many times we point at 0 during this rotation
        # Special case: if we start at 0, we only count times we HIT 0 during the move (not the start)
        
        if direction == 'L':
            # Moving left: how many times do we hit 0?
            if old_position == 0:
                # Starting at 0, moving left
                # We hit 0 at positions: 100, 200, 300, etc.
                if amount >= 100:
                    times_at_zero = amount // 100
                    count += times_at_zero
            else:
                # Not starting at 0
                # We hit 0 after old_position steps, then every 100 steps
                if amount >= old_position:
                    times_at_zero = 1 + ((amount - old_position) // 100)
                    count += times_at_zero
        else:  # direction == 'R'
            # Moving right: how many times do we hit 0?
            if old_position == 0:
                # Starting at 0, moving right
                # We hit 0 at positions: 100, 200, 300, etc.
                if amount >= 100:
                    times_at_zero = amount // 100
                    count += times_at_zero
            else:
                # Not starting at 0
                # We hit 0 when reaching positions: 100, 200, 300, ...
                total_distance = old_position + amount
                if total_distance >= 100:
                    times_at_zero = total_distance // 100
                    count += times_at_zero
    
    return count


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
