import numpy as np

# Test division
def division(a,b):
    return a/b

def test_answer():
    assert division(2,8) == 0.25

# Test division numpy
def numpy_divide(a,b):
    return np.array(a) / np.array(b)

def test_answer_numpy():
    assert numpy_divide(2,8) == 0.25
