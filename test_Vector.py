from Vector import Vector
import math

def test___iter__():
    v = Vector([1,2])
    it = iter(v)
    assert next(it) == 1

def test_tolist():
    v = Vector([1,2])
    assert v.tolist() == [1,2]

def test___add__():
    v1 = Vector([1,2])
    v2 = Vector([3,4])
    v3 = Vector([v1[0]+v2[0],v1[1]+v2[1]])
    assert v3.values == [4,6]

def test__norm():
    v = Vector([5,12])
    assert v.norm == 13

def test___eq__():
    v1 = Vector([1,2])
    v2 = Vector([1,2])
    assert v1.values == v2.values

def test___rmul__():
    v1 = Vector([1,2])
    v2 = Vector([v1[0],v1[1]])*3
    assert v2.values == [3,6]

def test___mul__():
    v1 = Vector([1,2])
    v2 = Vector([3,4])
    v3 = Vector([v1[0]*v2[0],v1[1]*v2[1]])
    assert v3.values == [3,8]

def test__getitem__():
    v = Vector([1,2])
    assert v.__getitem__(0) == 1