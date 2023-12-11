#Cart functionalites are defined below
class ShoppingCart:
    def __init__(self, discount_strategy=None):
        self.cart = {}
        self.discount_strategy = discount_strategy

    def add_to_cart(self, product):
      if product.get_id() not in [ y.get_id() for y in self.cart.keys()]:
        cloned_product = product.clone()
        self.cart[cloned_product] = 1
        print(f"{cloned_product.get_id()} successfully addedd to the cart.")
      else:
        print(f"{cloned_product.get_id()} already exists in your cart. Move on to update quantity action if required.")

    def view_cart(self):
      print("Shopping Cart:")
      for product, quantity in self.cart.items():
        print(f"PrductID:{product.get_id()}, Product Name: {product.get_name()},  Quantity: {quantity}, Price_per_item: {product.get_price()}")
      total_price=self.calculate_total_price()
      print(f"Total Price: ${total_price}")

    def calculate_total_price(self,total_price=0):
      if self.discount_strategy:
        print(f"Applied Discount Strategy: {self.discount_strategy.get_strategy_name()}")
        total_price=self.discount_strategy.apply_discount(self.cart)
      else:
        total_price = sum(product.get_price() * quantity for product, quantity in self.cart.items())
      return total_price

    def update_quantity(self, product_id, quantity):
      selected_product = next((p for p in self.cart.keys() if p.get_id() == product_id), None)
      if selected_product:
        self.cart[selected_product] = quantity
        print(f"Product with product Id {product_id} has been updated.")
      else:
        print(f"Product with product Id {product_id} does not exists in your cart")

    def remove_from_cart(self, product_id):
      selected_product = next((p for p in self.cart.keys() if p.get_id() == product_id), None)
      if selected_product:
        del self.cart[selected_product]
        print(f"Product with productId {product_id} has been removed from the cart.")
      else:
        print(f"Product with productId {product_id} does not exists in your cart")

    def checkout(self):
      self.view_cart()
      if input("Do you want to proceed to checkout? (yes/no): ").lower() == "yes":
        print("Checkout successful!")
        self.cart = {}
        return True
      else:
        print("Checkout canceled.")
        return False

    def is_empty(self):
      if len(self.cart)==0:
        return True
      else:
        return False
