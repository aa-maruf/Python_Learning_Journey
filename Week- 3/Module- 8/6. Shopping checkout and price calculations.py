class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, item, price, quantity) :
        self.cart.append({'item': item, 'price': price, 'quantity': quantity})
    def checkout(self,amount) :
        price = 0
        for item in self.cart:
            print(item)
            price += item['price'] * item['quantity']
        if amount < price :
            return f'Please provide {price - amount} money more'
        elif amount > price:
            return f'Here are the items and extra money {amount - price}'
        else :
            return f'Here are the items'

Shopping = Shopper('kuddus')
Shopping.add_to_cart("Mobile", 21000, 1)
Shopping.add_to_cart("tv", 40000, 1)
Shopping.add_to_cart("Glass", 2200, 3)

reply = Shopping.checkout(400000)
print(reply)

        
        