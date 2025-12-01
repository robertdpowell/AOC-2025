"""
Tests for Advent of Code - Sample 02 (Past Year Puzzle)
"""
import pytest
from .solution import parse_input, solve_part_one, solve_part_two


class TestSample02:
    """Test cases for Sample 02 solutions."""

    # Example input from the problem specification
    EXAMPLE_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    def test_parse_input(self):
        """Test that input parsing works correctly."""
        result = parse_input(self.EXAMPLE_INPUT)
        # Should return a list of tuples containing (x, y) pairs from valid mul(x,y) patterns
        assert result is not None
        assert len(result) == 4  # Four valid patterns: mul(2,4), mul(5,5), mul(11,8), mul(8,5)
        assert result[0] == (2, 4)
        assert result[1] == (5, 5)
        assert result[2] == (11, 8)
        assert result[3] == (8, 5)

    def test_solve_part_one_example(self):
        """Test Part One with example input from specification."""
        # Expected: 2*4 + 5*5 + 11*8 + 8*5 = 8 + 25 + 88 + 40 = 161
        expected = 161
        assert solve_part_one(self.EXAMPLE_INPUT) == expected

    def test_solve_part_two_example(self):
        """Test Part Two with example input from specification."""
        # Example: xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
        # Expected: 48 (2*4 + 8*5)
        # mul(2,4) is enabled = 8
        # don't() disables
        # mul(5,5) is disabled = skip
        # mul(11,8) is disabled = skip
        # do() enables
        # mul(8,5) is enabled = 40
        # Total: 8 + 40 = 48
        part_two_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        expected = 48
        assert solve_part_two(part_two_input) == expected

    # Additional test cases for edge cases

    def test_empty_string(self):
        """Test with empty input."""
        assert solve_part_one("") == 0

    def test_no_valid_patterns(self):
        """Test with string containing no valid mul patterns."""
        assert solve_part_one("mul[1,2]mul(1,2]mul(1;2)") == 0

    def test_single_valid_pattern(self):
        """Test with single valid pattern."""
        assert solve_part_one("mul(3,4)") == 12

    def test_with_zero(self):
        """Test pattern with zero as multiplier."""
        assert solve_part_one("mul(0,5)mul(3,0)") == 0

    def test_large_numbers(self):
        """Test with larger numbers."""
        assert solve_part_one("mul(100,200)") == 20000

    def test_adjacent_patterns(self):
        """Test with adjacent valid patterns."""
        assert solve_part_one("mul(2,3)mul(4,5)") == 26  # 6 + 20

    # Part Two additional tests

    def test_part_two_no_control_commands(self):
        """Test Part Two with no do()/don't() commands - should work like Part One."""
        assert solve_part_two("mul(2,4)mul(5,5)") == 33  # 8 + 25

    def test_part_two_starts_with_dont(self):
        """Test Part Two starting with don't() - first mul should be ignored."""
        assert solve_part_two("don't()mul(2,4)do()mul(3,5)") == 15  # 0 + 15

    def test_part_two_multiple_toggles(self):
        """Test Part Two with multiple state changes."""
        assert solve_part_two("mul(2,2)don't()mul(3,3)do()mul(4,4)don't()mul(5,5)") == 20  # 4 + 16

    def test_part_two_ends_disabled(self):
        """Test Part Two ending in disabled state."""
        assert solve_part_two("mul(2,4)don't()mul(5,5)") == 8  # Only first mul

    def test_part_two_empty_string(self):
        """Test Part Two with empty input."""
        assert solve_part_two("") == 0
