# Objective: The goal of this assignment is to demonstrate a deep understanding of inheritance and method overriding in Python. Students will apply these concepts to develop an E-commerce Product Catalog System that handles various types of products with both common and unique attributes.

# Problem Statement: An e-commerce platform requires a system to manage different types of products, such as books, electronics, and clothing. Each product type shares some common characteristics but also has unique features. The system should be able to display information about each product appropriately.


# Task 1: Create Base Product Class

# Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.
# Expected Outcome: A Product class that can hold general information about a product and display it.

#Task 1
class Product:
    def __init__(self, prod_id, name, price): 
        self.prod_id = prod_id
        self.name = name
        self.price= price

    def display_info(self):
        print(f"Product ID: {self.prod_id}")
        print(f'Name: {self.name}')
        print(f"Price: ${self.price}")

#Task2
class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

#Task3
    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")

# Example usage
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()