class Test:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"str() {self.name}-{self.price}"
    
    def __repr__(self):
        return f"repr() {str(self)}"
    

    def __eq__(self, other):
        return (self.name == other.name) and (self.price == other.price)
    
    def __hash__(self):
        return hash((self.name, self.price))
    
    def __getitem__(self, index):
        return self.name


t1= Test("aaa", 1000)
print(t1)
t2 = Test("aaa", 1000)
print(t1 == t2)

dict = {t1: t1.price, t2:t2.price}
print(dict)