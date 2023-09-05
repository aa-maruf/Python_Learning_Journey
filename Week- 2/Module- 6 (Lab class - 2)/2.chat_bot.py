""" 
chanbot.
steps :
1.input/ Listen
2. process/decide
3. output /talkback
 """
greet_words = ['hi', 'hello', 'yo']
bye_words = ['bye', 'tata', 'hasta la vista']
bad_words = ['dog', 'cow', 'idiot']

def listen():
    return input ("Say Something:")

def decide (command):
    command = command.lower()
    broken_words = command.split(" ") # white space paile word bangbe and list akare word gula store krbe.
    # print(broken_words)
    f = False
    for word in broken_words:
        if word in greet_words:
            talkback("Hi, man.")
            f |= 1
        elif word in bye_words:
            talkback("Okay, bye. Stay safe.😉")
            f |= 1
        elif word in bad_words:
            talkback("You are bad guy.Behave yourself")
            f |= 1
        elif f:
            break
def talkback(response):
    print(response)
   

command = listen()
decide(command)
# print(command)