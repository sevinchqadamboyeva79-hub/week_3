class ShoppingCart:
    def __init__(self,items=None):
        if items==None:
            self.items=[]
        else:
         self.items=items
    def add(self,name, price):
       return self.items.append((name,price))
    def __len__(self):
       return len(self.items)
    def __getitem__(self,index):
       return f'{self.items[index][0]}: {self.items[index][1]}'
    def __add__(self,other):
       new_card=self.items+other.items
       return ShoppingCart(new_card)
    def __eq__(self,other):
       total_price1=sum(price for name,price in self.items)
       total_price2=sum(price for name,price in other.items)
       return total_price1 == total_price2

cart1 = ShoppingCart()
cart1.add("Apple", 2.50)
cart1.add("Bread", 3.00)

cart2 = ShoppingCart()
cart2.add("Milk", 4.50)
cart2.add("Eggs", 1.00)

print(len(cart1))
print(cart1[0])
print(cart1)

cart3 = cart1 + cart2
print(cart3)
print(len(cart3))

print(cart1 == cart2)

empty = ShoppingCart()
if not empty:
    print("Cart is empty")      
          
          
       
    
       
       
       

        




