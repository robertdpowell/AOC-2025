import sys
from pathlib import Path


def parse_input(input_data: str) -> list:
    """Parse input into list of (direction, amount) tuples."""
    if not input_data.strip():
        return []
    return [(line[0], int(line[1:])) for line in input_data.strip().split('\n') if line.strip()]


def solve_part_one(input_data: str) -> int:
    """Count times position stops at 0 on circular dial (0-99)."""
    instructions = parse_input(input_data)
    position = 50
    zero_count = 0
    
    for direction, amount in instructions:
        position = (position - amount if direction == 'L' else position + amount) % 100
        if position == 0:
            zero_count += 1
    
    return zero_count


def solve_part_two(input_data: str) -> int:
    """Count stops and crossings at 0 during dial movement."""
    instructions = parse_input(input_data)
    position = 50
    count = 0
    
    for direction, amount in instructions:
        old_position = position
        position = (position - amount if direction == 'L' else position + amount) % 100
        
        if direction == 'L':
            if old_position == 0:
                count += amount // 100 if amount >= 100 else 0
            elif amount >= old_position:
                count += 1 + ((amount - old_position) // 100)
        else:
            if old_position == 0:
                count += amount // 100 if amount >= 100 else 0
            else:
                total_distance = old_position + amount
                count += total_distance // 100 if total_distance >= 100 else 0
    
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
