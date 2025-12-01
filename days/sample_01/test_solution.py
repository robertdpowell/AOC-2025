"""
Tests for Advent of Code - Sample 01 (Past Year Puzzle)
"""
import pytest
from .solution import parse_input, solve_part_one, solve_part_two


class TestSample01:
    """Test cases for Sample 01 solutions."""

    # Example input from the problem specification
    EXAMPLE_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""

    def test_parse_input(self):
        """Test that input parsing works correctly."""
        result = parse_input(self.EXAMPLE_INPUT)
        # Should parse into two lists of numbers
        assert result is not None
        assert len(result) == 2  # Two lists
        assert len(result[0]) == 6  # Six numbers in first list
        assert len(result[1]) == 6  # Six numbers in second list
        # Verify the first list contains the left column
        assert result[0] == [3, 4, 2, 1, 3, 3]
        # Verify the second list contains the right column
        assert result[1] == [4, 3, 5, 3, 9, 3]

    def test_solve_part_one_example(self):
        """Test Part One with example input from specification."""
        # Expected: 2 + 1 + 0 + 1 + 2 + 5 = 11
        expected = 11
        assert solve_part_one(self.EXAMPLE_INPUT) == expected

    def test_solve_part_two_example(self):
        """Test Part Two with example input from specification."""
        # Expected: 31 (9 + 4 + 0 + 0 + 9 + 9)
        # For each number in left list, count occurrences in right list and multiply
        # 3 appears 3 times in right: 3 * 3 = 9
        # 4 appears 1 time in right: 4 * 1 = 4
        # 2 appears 0 times in right: 2 * 0 = 0
        # 1 appears 0 times in right: 1 * 0 = 0
        # 3 appears 3 times in right: 3 * 3 = 9
        # 3 appears 3 times in right: 3 * 3 = 9
        # Total: 9 + 4 + 0 + 0 + 9 + 9 = 31
        expected = 31
        assert solve_part_two(self.EXAMPLE_INPUT) == expected

    # Additional test cases can be added below
    # based on edge cases identified in the specification
