from src.assignment import *
from io import StringIO
import sys

def test_get_sum():
    assert get_sum(1, 2) == 3
    assert get_sum(-1, -2) == -3
    assert get_sum(5, -3) == 2
    assert get_sum(0, 0) == 0
    assert get_sum(1000000, 2000000) == 3000000


def test_greet():
    # Redirect standard output to capture prints
    captured_output = StringIO()
    sys.stdout = captured_output

    # Test cases
    greet("Alice")
    assert captured_output.getvalue().strip() == "Hello, Alice !"

    captured_output = StringIO()
    sys.stdout = captured_output
    greet("Bob")
    assert captured_output.getvalue().strip() == "Hello, Bob !"

    captured_output = StringIO()
    sys.stdout = captured_output
    greet("Charlie")
    assert captured_output.getvalue().strip() == "Hello, Charlie !"

    # Restore standard output
    sys.stdout = sys.__stdout__