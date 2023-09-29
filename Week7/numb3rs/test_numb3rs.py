from numb3rs import validate
import pytest

def main():
    test_length()
    test_range()
    test_numeric()
    test_firstByte()


def test_length():
    assert validate('1.1.1')==False

def test_range():
    assert validate('100.1.1.1')==True

def test_firstByte():
    assert validate('275.1.0.0')==False

def test_numeric():
    assert validate('cat')==False


if __name__ == "__main__":
    main()