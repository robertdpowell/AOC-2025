# Implement Solution and Pass Tests

Read the SPECIFICATION.md file and implement a solution in solution.py that passes all tests.

## Instructions

1. **Read the SPECIFICATION.md file** in the current day folder to understand:
   - The problem description for Part One and Part Two
   - The algorithm or logic required to solve the problem
   - Any constraints or special conditions

2. **Review the test file** (test_solution.py) to understand what the tests expect.

3. **Implement the solution in solution.py:**
   - Update `parse_input()` to correctly parse the input data into a suitable data structure
   - Implement `solve_part_one()` to solve Part One of the puzzle
   - Implement `solve_part_two()` to solve Part Two of the puzzle

4. **Run the tests** with `pytest days/day_XX/ -v` after each change to verify progress.

5. **Iterate until all tests pass:**
   - If a test fails, analyze the error message
   - Adjust the implementation accordingly
   - Re-run the tests
   - Repeat until all tests pass
   - Then run the solution against the actual puzzle input to get the final answers
   - Tell me the final answers for Part One and Part Two

6. **Code quality:**
   - Keep the code readable and well-documented
   - Use meaningful variable names
   - Add comments to explain complex logic

## Example Implementation Pattern

```python
def parse_input(input_data: str) -> list:
    """Parse the input into a usable data structure."""
    lines = input_data.strip().split('\n')
    # Transform lines as needed for the problem
    return parsed_data

def solve_part_one(input_data: str) -> int:
    """Solve Part One."""
    data = parse_input(input_data)
    # Implement the algorithm for Part One
    return result

def solve_part_two(input_data: str) -> int:
    """Solve Part Two."""
    data = parse_input(input_data)
    # Implement the algorithm for Part Two
    return result
```

## Running Tests

```bash
# Run tests for the current day
pytest days/day_XX/ -v

# Run tests with output displayed
pytest days/day_XX/ -v -s
```
