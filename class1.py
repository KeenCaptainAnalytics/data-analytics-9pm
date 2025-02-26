# class

class Car :
    def __init__(self, para_brand, para_model, para_color,para_price ) :
        self.brand = para_brand
        self.model = para_model
        self.color = para_color
        self.price = para_price

    def print_info(self):
        print(self.price, self.color, self.model, self.brand)


car1obj = Car("tata", "1234","black", 200000 )
car2obj = Car("Maruti", "13434","white", 500000 )

car1obj.print_info()
car2obj.print_info()

# print(car1obj.model,car1obj.brand, car1obj.color, car1obj.price)
# print(car2obj.model,car2obj.brand, car2obj.color, car2obj.price)
