class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.shoe_type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
        self.laces_tied = False
        
        # methods are actions that can be taken on the instance
    def tie_laces(self):
        # if (self.laces_tied  == False):
        if not self.laces_tied:
            print("Tieing the laces")
            self.laces_tied = True
        else:
            print("already tied the laces")
        
myShoe = Shoe('Nike', 'running', 230)
print(myShoe.brand)
print(myShoe.shoe_type)
print(myShoe.price)
print(myShoe.laces_tied)

#target | #!method
myShoe.tie_laces()
print(myShoe.laces_tied)
myShoe.tie_laces()