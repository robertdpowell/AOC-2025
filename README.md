# Advent of Code 2025

A Python-based repository for solving Advent of Code 2025 puzzles using a specification-driven/test-driven development approach.

## Project Structure

```
AOC-2025/
├── README.md
├── requirements.txt
└── days/
    ├── day_01/
    │   ├── SPECIFICATION.md    # Problem statement and examples
    │   ├── test_solution.py    # Test cases for the solution
    │   └── solution.py         # Solution implementation
    ├── day_02/
    │   └── ...
    └── day_12/
        └── ...
```

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Workflow for Each Day

### 1. Specification

Copy the problem statement from adventofcode.com to `days/day_XX/SPECIFICATION.md`. Include:
- Problem description for Part One and Part Two
- Example inputs and expected outputs
- Any notes or observations about edge cases

### 2. Write Tests

Based on the specification, update `days/day_XX/test_solution.py`:
- Add example input data
- Write test cases for parsing
- Write test cases with expected outputs from examples

### 3. Implement Solution

Implement the solution in `days/day_XX/solution.py`:
- Complete the `parse_input()` function
- Implement `solve_part_one()`
- Implement `solve_part_two()`

### 4. Run Tests

```bash
# Run all tests
pytest

# Run tests for a specific day
pytest days/day_01/

# Run tests with verbose output
pytest -v

# Run tests with output displayed
pytest -s
```

### 5. Run Solution

```bash
# Navigate to day directory and run
cd days/day_01
python solution.py
```

Or from the root directory:
```bash
python -m days.day_01.solution
```

## License

This project is for personal educational purposes as part of the Advent of Code 2025 challenge.