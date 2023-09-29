from seasons import convert
import pytest

def main():
    test_convert()


def test_convert():
    assert convert('1999-12-31')== 'Twelve million, two hundred thirty-four thousand, two hundred forty'
    assert convert('1999-01-01')== 'Twelve million, seven hundred fifty-eight thousand, four hundred'
   




if __name__ == "__main__":
    main()