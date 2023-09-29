from fuel import convert, gauge
import pytest



def main():
    test_convert()
    test_gauge()
    test_exeption()

def test_convert():
    assert convert('2/3')==67
    assert convert('1/100')==1
    assert convert('99/100')==99
    assert convert('3/4')==75


def test_gauge():
    assert gauge(67)=='67%'
    assert gauge(1)=='E'
    assert gauge(99)=='F'
    assert gauge(75)=='75%'

def test_exeption():
    with pytest.raises(ValueError):
        convert('10/9')
    with pytest.raises(ZeroDivisionError):
        convert('9/0')
    with pytest.raises(ValueError):
        convert('cat/dog')


if __name__ == "__main__":
    main()