from abc import ABC, abstractmethod


# ================= PRODUCT =================

class Product(ABC):

    total_products = 0

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.__price = price
        self.__quantity = quantity

        Product.total_products += 1

    # Encapsulation
    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative")

    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            print("Quantity cannot be less than 0")

    @classmethod
    def get_total_products(cls):
        return cls.total_products

    @staticmethod
    def calculate_gst(amount):
        return amount * 0.18

    @abstractmethod
    def display_product(self):
        pass

    @abstractmethod
    def calculate_discount(self):
        pass
    
    # ================= ELECTRONICS =================

class Electronics(Product):

    def __init__(self, product_id, name, price, quantity,
                 brand, warranty_years):
        super().__init__(product_id, name, price, quantity)

        self.brand = brand
        self.warranty_years = warranty_years

    def display_product(self):
        print(f"{self.product_id}.{self.name}({self.brand})-{self.get_price()}")

    def calculate_discount(self):
        if self.get_price() > 50000:
            return 15
        return 5


# ================= CLOTHING =================

class Clothing(Product):

    def __init__(self, product_id, name, price,
                 quantity, category, size, fabric_type):

        super().__init__(product_id, name, price, quantity)

        self.category = category
        self.size = size
        self.fabric_type = fabric_type

    def display_product(self):
        print(f"{self.product_id}:{self.name}({self.size})-{self.get_price()}")

    def calculate_discount(self):
        if self.get_price() > 3000:
            return 20
        return 10