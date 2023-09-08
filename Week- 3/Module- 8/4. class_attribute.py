""" 
# Class vitore direct instance or attribute rakle ogula static hoye jay, 
# means sob object er jonno same hbe. Kono ekta object attribute er value  change krle bikder jonno o same dekhabe.
#  tai attribute normally __init__ er through declare kra hoy.Even onno class function er through o kra jay.
# Ekta class function er bhitore onno arekta class function ke call kra jay.
# __dic__ diye ekta object sob gula attribute dekha jay.
"""
class shop :
    cart = []   # cart is class attribute (static) , Equal for all.

    def __init__(self, buyer)  :
        self.buyer = buyer
    
    def add_to_cart(self,item) :
        self.cart.append(item)

my_shop = shop("Kamal")
my_shop.add_to_cart("Apple")

dad_shop = shop ("Jon")
dad_shop.add_to_cart("Nokia")

print(my_shop.cart)      # apple , nokia both will be shown in list because it is static
print(dad_shop.cart)

class Laptop:
    def __init__(self, brand , age) :  
        self.brand = brand             # declaring and assigning brand and age attribute of laptop 
        self.age = age  
    
    def increase_age(self, life_increase = 1) :
        self.last_age = self.age # declaring attribute in function
        self.age = life_increase + self.age
    def repair (self, life_increase = -5) :
        self.increase_age(life_increase)

my_laptop = Laptop("Acer", 1.5)
my_laptop.increase_age()
my_laptop.age = 17
my_laptop.increase_age()
my_laptop.increase_age()
my_laptop.repair(-7)
print(my_laptop.age)
print(my_laptop.__dict__)

