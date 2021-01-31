import pytest


def test_demo_1():
    assert 1 == 1


def test_demo_fail_1():
    assert 1 == 2


def test_skip():
    assert pytest.skip('skip')

@pytest.mark.parametrize('a,b,c', [
    [1,2,3],
    [3,4,7],
    [1,3,5]
])
def test_params(a,b,c):
    assert a+b == c