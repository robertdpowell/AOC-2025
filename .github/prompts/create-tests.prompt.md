# Create Tests Based on the Specification

Read the SPECIFICATION.md file in the current day's folder and create comprehensive tests in test_solution.py. Bear in mind that part two may not always be present as we need to first complete part one and only then do we have the puzzle for part two.

## Instructions

1. **Read the SPECIFICATION.md file** in the current day folder to understand:
   - The problem description for Part One or Part Two
   - Example inputs and their expected outputs
   - Any edge cases or special conditions mentioned

2. **Update test_solution.py** with:
   - The example input data from the specification in `EXAMPLE_INPUT`
   - A test for `parse_input()` that verifies input parsing works correctly
   - A test for `solve_part_one()` using the example input and expected output
   - A test for `solve_part_two()` using the example input and expected output
   - Additional edge case tests if any are identified in the specification

3. **Test structure to follow** (replace XX with the actual day number, e.g., 01, 02):
   ```python
   class TestDayXX:
       EXAMPLE_INPUT = """<paste example input here>"""

       def test_parse_input(self):
           result = parse_input(self.EXAMPLE_INPUT)
           # Assert the parsed structure is correct

       def test_solve_part_one_example(self):
           expected = <expected_value_from_spec>
           assert solve_part_one(self.EXAMPLE_INPUT) == expected

       def test_solve_part_two_example(self):
           expected = <expected_value_from_spec>
           assert solve_part_two(self.EXAMPLE_INPUT) == expected
   ```

4. **Run the tests** with `pytest days/day_XX/ -v` to confirm they fail as expected (since the solution is not yet implemented).
