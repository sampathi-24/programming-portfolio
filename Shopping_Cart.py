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
    
# ================= SHOPPING CART =================

class ShoppingCart:

    def __init__(self):
        self.cart = []

    # Aggregation
    def add_product(self, product, qty):
        self.cart.append((product, qty))
        print(f"{qty} products are added to cart")

    def remove_product(self, product_id):

        for item in self.cart:
            product, qty = item

            if product.product_id == product_id:
                self.cart.remove(item)
                print("Product removed")
                return

    def display_cart(self):

        if not self.cart:
            print("Cart is Empty")
            return

        print("-" * 66)
        print("product  product   Price Quantity Total   Discount  After_Discount")
        print("_id      _name                     _price  Applied       Price")
        print("-" * 66)

        grand_total = 0

        for product, qty in self.cart:

            total_price = product.get_price() * qty

            discount_percent = product.calculate_discount()

            discount_amount = total_price * discount_percent / 100

            grand_total += (total_price - discount_amount)

            print(
                f"{product.product_id:<8}"
                f"{product.name:<10}"
                f"{product.get_price():<8}"
                f"{qty:<8}"
                f"{total_price:<10}"
                f"{str(discount_percent)+'%':<10}"
                f"{discount_amount:.0f}"
            )

        return grand_total

    def calculate_total(self):

        total = 0

        for product, qty in self.cart:
            total += product.get_price() * qty

        return total

    def apply_all_discounts(self):

        final_total = 0

        for product, qty in self.cart:

            total = product.get_price() * qty

            discount = total * product.calculate_discount() / 100

            final_total += (total - discount)

        return final_total

    # Operator Overloading
    def __add__(self, other):
        return self.calculate_total() + other.calculate_total()


# ================= PRODUCTS =================

electronics = [
    Electronics(121, "laptop", 50000, 1, "dell", 2),
    Electronics(212, "Mobile", 15000, 1, "vivo", 1),
    Electronics(332, "charger", 6000, 1, "samsung", 1)
]

mens = [
    Clothing(123, "shirt", 5000, 1, "Mens", "L", "Cotton"),
    Clothing(232, "pant", 6000, 1, "Mens", "L", "Denim")
]

womens = [
    Clothing(341, "kurti", 3500, 1, "Womens", "M", "Rayon"),
    Clothing(452, "saree", 7000, 1, "Womens", "Free Size", "Silk")
]

kids = [
    Clothing(561, "T-Shirt", 1500, 1, "Kids", "S", "Cotton"),
    Clothing(672, "Shorts", 1200, 1, "Kids", "S", "Polyester")
]

cart = ShoppingCart()