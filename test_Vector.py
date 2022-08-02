from torch import true_divide
import Vector

def test___eq__():
    v1 = [1,2]
    v2 = [1,2]
    expected_result = True
    actual_result = Vector.__eq__(v1, v2)
    assert expected_result == actual_result