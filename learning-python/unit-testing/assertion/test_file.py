from addition import addition

def test_addition_int():
    assert addition(4, 5) == 9
    assert addition(12, 2) == 14

def test_addition_str():
    assert addition('a', 'b') == 'ab'
