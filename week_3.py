class StockItem:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"{self.name}: {self.quantity} in stock at ${self.price}"
    def __repr__(self):
        return f"StockItem('{self.name}', {self.price}, {self.quantity})"
    def __add__(self, value):
        if isinstance(value, StockItem):
            if self.name == value.name:         
                return StockItem(self.name, self.price, self.quantity + value.quantity)
            else:
                return NotImplemented
        elif isinstance(value, int):
            return StockItem(self.name, self.price, self.quantity + value)
        else:
            return NotImplemented
    def __eq__(self, other):
        if isinstance(other, StockItem):
            if self.name == other.name and self.price == other.price:  
                return True
            else:
                return False                     
        return NotImplemented                   
    def __bool__(self):
        if self.quantity > 0:
            return True
        return False                              

item1 = StockItem("Apples", 2.5, 10)
item2 = StockItem("Apples", 2.5, 15)
item3 = StockItem("Bananas", 3.0, 0)

print(str(item1))      
print(repr(item1))     
print(item1 + item2)   
print(item1 + 5)        
print(item1 == item2) 
print(bool(item1))      
print(bool(item3))      