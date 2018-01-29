from __future__ import division
import numpy as np

# Test division
def builtin_division(a,b):
    return a/b

def test_answer():
    assert builtin_division(2,8) == 0.25

# Test division numpy
def numpy_divide(a,b):
    return np.true_divide(a,b)

def test_answer_numpy():
    a = np.array([2])
    b = np.array([8])
    assert numpy_divide(a,b) == 0.25