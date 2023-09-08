# Method ke class er vitore dite gele parameter hishebe (self) dite hbe. Naile error!?
# you can use multiple parameter but must use the self along with those. (self, number, text)

class calculator :
    def add(self, a, b):
        return a + b
    def substract (self, a, b):
        return abs(a-b)
    def multiply (self, a, b) :
        return a*b
    def devide (self, a, b):
        return a/b
    
a = 10
b = 5
cal = calculator()
print(cal.add(a,b))
print(cal.substract(a,b))
print(cal.multiply(a,b))
print(cal.devide(a,b))
