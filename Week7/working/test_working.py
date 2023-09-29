from working import convert
import pytest

def main():
    test_noMinutes()
    test_AM()
    test_exeption()



def test_noMinutes():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"

def test_AM():
    assert convert("8 PM to 8 AM")=="20:00 to 08:00"

def test_exeption():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")



if __name__ == "__main__":
    main()