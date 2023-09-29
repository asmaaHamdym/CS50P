from plates import is_valid

def test_first_two():
    assert is_valid('CS50')==True
    assert is_valid('0950')==False


def test_alphnumeric():
    assert is_valid('PI3.14')==False
    assert is_valid('NRVOUS')==True
    assert is_valid('CS50P2')==False


def test_range():
    assert is_valid('OUTATIME')==False
    assert is_valid('H')==False


def test_number():
    assert is_valid('ECTO88')==True


def test_zero():

    assert is_valid('CS05')==False