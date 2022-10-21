from re_img import generate_img, check_extension
import pytest

def test_check_extension():
    with pytest.raises(SystemExit) as e:
        check_extension(".py")
    assert e.type == SystemExit

def test_generate_img():
    assert generate_img('doge1.jpeg', '.jpeg') == True
    

        