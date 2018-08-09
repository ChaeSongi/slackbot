import random


def test_plus():
    expected = "불렀어?"
    actual = answer("송이")
    assert expected == actual

def test_roll_a_die():
    expected = {"1","2","3","4","5","6"}
    actual = set()
    for i in range(1000):
        actual.add(answer("주사위"))
    assert expected == actual


def test_do_nothing_for_unknown_patterns():
    actual = answer("우웅웅웅!")
    assert actual is None
