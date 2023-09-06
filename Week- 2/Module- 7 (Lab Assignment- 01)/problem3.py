""" 3. Go to this repo: https://pypi.org/project/pyjokes/ and try to make a chat bot to tell you joke using pyjokes.
Write a function named tell_some_jokes() and write your code inside this function.
 """

import pyjokes
import time

def tell_some_jokes():
    print("Delicious Jokes For you:")
    time.sleep(2)
    print(pyjokes.get_joke())
    print("____   ____    ____")


while True:
    tell_some_jokes()
    time.sleep(5)
    flag = input(f'Type pyjoke for more jokes 🤞 :')
    if flag != "pyjoke":
        break
