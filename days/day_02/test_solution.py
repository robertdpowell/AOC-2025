"""
Tests for Advent of Code 2025 - Day 02
"""
import pytest
from .solution import parse_input, solve_part_one, solve_part_two


class TestDay02:
    """Test cases for Day 02 solutions."""

    EXAMPLE_INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

    def test_parse_input(self):
        """Test that input parsing works correctly."""
        result = parse_input(self.EXAMPLE_INPUT)
        assert result is not None
        assert len(result) == 11
        assert result[0] == (11, 22)
        assert result[1] == (95, 115)
        assert result[2] == (998, 1012)
        assert result[3] == (1188511880, 1188511890)
        assert result[4] == (222220, 222224)

    def test_solve_part_one_example(self):
        """Test Part One with example input from specification."""
        expected = 1227775554
        assert solve_part_one(self.EXAMPLE_INPUT) == expected

    def test_solve_part_two_example(self):
        """Test Part Two with example input from specification."""
        expected = 4174379265
        assert solve_part_two(self.EXAMPLE_INPUT) == expected

    def test_single_range_with_repeating_numbers(self):
        """Test a single range containing repeating pattern numbers."""
        assert solve_part_one("11-22") == 11 + 22

    def test_single_range_no_repeating_numbers(self):
        """Test a single range with no repeating patterns."""
        assert solve_part_one("12-20") == 0

    def test_repeating_digit_patterns(self):
        """Test various repeating digit patterns."""
        assert solve_part_one("55-55") == 55
        assert solve_part_one("99-99") == 99
        assert solve_part_one("7777-7777") == 7777

    def test_repeating_sequence_patterns(self):
        """Test repeating sequence patterns."""
        assert solve_part_one("123123-123123") == 123123
        assert solve_part_one("1010-1010") == 1010

    def test_range_with_mix(self):
        """Test range with both repeating and non-repeating numbers."""
        result = solve_part_one("10-12")
        assert result == 11

    def test_empty_input(self):
        """Test with empty input."""
        assert solve_part_one("") == 0

    def test_large_numbers_with_patterns(self):
        """Test large numbers with repeating patterns."""
        assert solve_part_one("1188511885-1188511885") == 1188511885
        assert solve_part_one("222222-222222") == 222222
