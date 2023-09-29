from um import count
import pytest

def main():
    test_space()
    test_caps()
    test_partofWord()
    


def test_space():
    assert count('um  ')==1

def test_caps():
    assert count('Um, oh')==1

def test_partofWord():
    assert count('album')==0




if __name__ == "__main__":
    main()
