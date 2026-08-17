# app.py
# This is a test commit
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-1, 4) == -4
