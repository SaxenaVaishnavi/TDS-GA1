import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test a list with multiple positive streaks, ensuring the longest is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_positive():
    """Test a list where all numbers are positive."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_no_positive():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_single_element_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_streak_at_beginning():
    """Test when the longest streak is at the beginning of the list."""
    assert longest_positive_streak([4, 5, 6, -1, 2]) == 3

def test_streak_at_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, -5, 3, 4, 5, 6]) == 4

def test_zeros_and_negatives_breaking_streak():
    """Test that zeros and negative numbers correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, -5, 6]) == 2