import pytest
from streak import longest_positive_streak

def test_single_case():
    """A single, simple test case for debugging."""
    assert longest_positive_streak([1, 2, -1, 4, 5, 6]) == 3