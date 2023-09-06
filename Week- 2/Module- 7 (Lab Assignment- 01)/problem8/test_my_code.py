# type pyTest
# test_my_code.py
import problem8
def test_script():
    assert problem8.make_upper("HeLLo") == "HELLO"
    assert problem8.make_lower("HeLLo") == "hello"
    assert problem8.make_capital("HeLLo") == "Hello"

