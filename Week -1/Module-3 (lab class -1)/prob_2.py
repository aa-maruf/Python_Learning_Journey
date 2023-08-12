"""  Encrypt the following code so that no one can get your strategy.
 """
data = "jmvifefec"
shift = 4
output = ''

for c in data :
    output += chr((ord(c) - shift - 97 ) % 26 + 97)

print(output)