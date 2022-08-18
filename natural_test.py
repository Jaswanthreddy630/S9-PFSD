import pytest
def fn(y):
    return y * (y + 1) / 2
def test_ans():
    assert fn(3)==6
