
class Phone:
    manufactured = "China"
    def __init__(self, brand, price, color) : # __int__ is alternative of constructor 
        self.brand = brand
        self.price = price
        self.color = color

my_phone = Phone("Oppo",13000, 'blue')
print(my_phone.brand, my_phone.color,my_phone.manufactured)
dad_phone = Phone("Nokia", 15000, "Black")
print(dad_phone.brand,dad_phone.color, dad_phone.manufactured)