import pytest
from calculator import add, subtract, multiply, divide

# HOW A TEST WORKS
#   1. The function name MUST start with `test_` so pytest finds it.
#   2. Call your code with some input.
#   3. `assert` what the answer should be. If the assert is False, the test fails.
#
# Run all tests:   pytest
# Run with detail: pytest -v


# SAMPLE TEST (done for you) 
def test_add():
    assert add(2, 3) == 5          # normal case
    assert add(-2, -3) == -5       # negative numbers
    assert add(-4, 10) == 6        # mixed signs
    assert add(0, 0) == 0          # zero
    assert add(2.5, 0.5) == 3.0    # decimals


# YOUR TURN
# Write the tests below. Follow the same pattern as test_add.


# TODO: write test_subtract()


# TODO: write test_multiply()


# TODO: write test_divide()


# TODO: write test_divide_by_zero()
#   divide() raises a ValueError when b is 0. Here's how to test for an error:
#       with pytest.raises(ValueError):
#           divide(1, 0)


# BONUS: add any extra tests you want! 