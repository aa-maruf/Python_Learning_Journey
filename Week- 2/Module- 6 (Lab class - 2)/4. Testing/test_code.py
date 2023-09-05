""" 
# installed  pytest
# write on terminal:  pytest
# It shows how many functions ran successfully 

"""
import my_code
# from my_code import AlphabetSerial  # eta use krleo  Don't copy ta print hoy!

print(my_code.AlphabetSerial('D'))

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def  test_getresponse():
    ret = my_code.get_response(api_url)
    assert ret.status_code == 200             # write pytest it returns function status then again run with status_code == 190 , see the difference

def test_again():
    assert 3 == 3 