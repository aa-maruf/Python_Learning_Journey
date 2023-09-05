import requests
api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def get_response(url):
    return requests.get(url)

def AlphabetSerial (ch):
    ch = ch.lower()
    return ord(ch) - 96   # To make a = 1 subtracted 1 with 97

res = get_response(api_url)  # res = 200
print(res) 
print(AlphabetSerial("Z"))



print("Don't copy from here!")
if __name__ == "__main__" :
    print("Prevents copying from here.")
    


