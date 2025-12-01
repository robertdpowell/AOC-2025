"""
Tests for Advent of Code 2025 - Day 01
"""
import pytest
from .solution import parse_input, solve_part_one, solve_part_two


class TestDay01:
    """Test cases for Day 01 solutions."""

    # Example input from the problem specification
    EXAMPLE_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    def test_parse_input(self):
        """Test that input parsing works correctly."""
        result = parse_input(self.EXAMPLE_INPUT)
        # Should return a list of tuples (direction, amount)
        assert result is not None
        assert len(result) == 10  # 10 instructions in example
        assert result[0] == ('L', 68)
        assert result[1] == ('L', 30)
        assert result[2] == ('R', 48)
        assert result[3] == ('L', 5)
        assert result[9] == ('L', 82)

    def test_solve_part_one_example(self):
        """Test Part One with example input from specification."""
        # Starting at position 50, count times position is 0
        # Expected output: 3
        expected = 3
        assert solve_part_one(self.EXAMPLE_INPUT) == expected

    def test_solve_part_two_example(self):
        """Test Part Two with example input from specification."""
        # Should count both stops at 0 and crossings over 0
        # Expected: 3 stops + 3 crossings = 6 total
        expected = 6
        assert solve_part_two(self.EXAMPLE_INPUT) == expected

    # Additional test cases for edge cases

    def test_empty_input(self):
        """Test with no instructions."""
        assert solve_part_one("") == 0

    def test_single_instruction_no_zero(self):
        """Test single instruction that doesn't reach 0."""
        assert solve_part_one("R10") == 0  # 50 + 10 = 60, never hits 0

    def test_single_instruction_lands_on_zero(self):
        """Test single instruction that lands exactly on 0."""
        assert solve_part_one("L50") == 1  # 50 - 50 = 0

    def test_single_instruction_crosses_zero(self):
        """Test single instruction that crosses through 0."""
        assert solve_part_one("L60") == 0  # 50 - 60 = -10, crosses but doesn't land on 0

    def test_back_and_forth_through_zero(self):
        """Test moving back and forth across 0."""
        # Start at 50, L60 → -10 (crosses 0, doesn't land)
        # R20 → 10 (crosses 0 again, doesn't land)
        assert solve_part_one("L60\nR20") == 0

    def test_landing_on_zero_twice(self):
        """Test landing on 0 multiple times."""
        # Start at 50, L50 → 0 (count=1)
        # R100 → 0 (count=2), L100 → 0 (count=3)
        assert solve_part_one("L50\nR100\nL100") == 3

    def test_all_left_moves(self):
        """Test only moving left from start position."""
        # Start at 50, L10 → 40, L10 → 30, L10 → 20, L10 → 10, L10 → 0
        assert solve_part_one("L10\nL10\nL10\nL10\nL10") == 1

    def test_all_right_moves(self):
        """Test only moving right (never reaching 0)."""
        assert solve_part_one("R10\nR20\nR30") == 0

    def test_starting_near_zero(self):
        """Test when close to 0 initially."""
        # Start at 50, L49 → 1, L2 → -1 (crosses 0, doesn't land)
        assert solve_part_one("L49\nL2") == 0
