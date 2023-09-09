class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def view_cart(self):
        for item in self.items:
            print(f"{item['product'].name} - ${item['product'].price} x{item['quantity']}")
    
    def compute_order_total(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items)
        return total

    def checkout(self):
        total = self.compute_order_total()
        print(f"Order total: ${total}")
        payment_method = input("Enter payment method (credit card, PayPal, etc.): ")
        print(f"Payment processed using {payment_method}. Order placed!")

# Create some sample products
product1 = Product("Product A", 10.99)
product2 = Product("Product B", 5.99)
product3 = Product("Product C", 7.49)

# Create a shopping cart
cart = ShoppingCart()

# Add products to the cart
cart.add_item(product1, 2)
cart.add_item(product2)
cart.add_item(product3, 3)

# View the cart contents
print("Cart contents:")
cart.view_cart()

# Compute and display the order total
total = cart.compute_order_total()
print(f"Order total: ${total}")

# Checkout
cart.checkout()
