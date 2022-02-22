class Laptop:
    def __init__(self,name,model_no,price):
        self.__name =name
        self.model_no= model_no
        self.price=price
l1=Laptop("lenovo",123,50000)
print(l1.__name)