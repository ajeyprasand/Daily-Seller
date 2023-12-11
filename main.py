from discount_strategies import *
from product import *
from shopping_cart import *
from system_utils import *

# Main Program starts here
if __name__=="__main__":
  print("_____Welcome to Daily Seller_____")
  #cart creation
  shopping_cart = ShoppingCart(BuyOneGetOneFree())

  #product creation
  electronic_product = Electronic_Product("Laptop", 1000)
  health_product = Medicinal_Product("Vitamin C", 10)
  textile_product = Textile_Product("T-Shirt", 20)

  #directing user to the system only if there are products listed
  flag = Product.display_created_products()
  if flag:
    if shopping_cart.discount_strategy.get_strategy_name():
      print(f"Hot deal today:{shopping_cart.discount_strategy.get_strategy_name()}")
    user_interface(shopping_cart)
