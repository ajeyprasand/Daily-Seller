def validate_quantity(quantity):
  try:
    quantity = int(quantity)
    if quantity<=0:
      print("Quantity must be greater than 0")
      return False,0
    return True,quantity
  except ValueError:
    print("Quantity must be Positive whole number")
    return False,0

def user_interface(shopping_cart):
  print("--------------")
  print("Actions Menu:")
  actions = [
        '1. Add to Cart',
        '2. View Cart',
        '3. Update Cart',
        '4. Remove from Cart',
        '5. Checkout',
        '6. Exit'
    ]
  for action in actions:
    print(f"\t{action}")
  while True:
    try:
      choice=int(input("Enter action(number from menu): "))
      if choice not in range(1,7):
        print("Please choose a action from the given menu")
      else:
        #Adding a product to the cart
        if choice==1:
          product_id = input("Enter the ID of the product to add to the cart: ").strip()
          selected_product = next((p for p in Product.product_registry if p.get_id() == product_id), None)
          if selected_product:
            shopping_cart.add_to_cart(selected_product)
          else:
            print(f"Product with the productID {product_id} does not exists")

        #Display cart
        if choice==2:
          if shopping_cart.is_empty():
            print("Your shopping cart is empty")
          else:
            shopping_cart.view_cart()

        #Updating quantity of item in Cart
        if choice==3:
          if shopping_cart.is_empty():
            print("Your shopping cart is empty. Cannot proceed to action")
          else:
            try:
              user_input = input("Enter the ID of the product to update in the cart and quantity (comma seperated) : ").strip()
              product_id,quantity = user_input.split(',')
              flag, quantity = validate_quantity(quantity)
              if flag:
                shopping_cart.update_quantity(product_id.strip(),quantity)
            except ValueError:
              print("Value for updating a product must be entered in the requested format")

        #Removing Product from the Cart
        if choice==4:
          if shopping_cart.is_empty():
            print("Your shopping cart is empty. Cannot proceed to action")
          else:
            product_id = input("Enter the ID of the product to remove from the cart: ").strip()
            shopping_cart.remove_from_cart(product_id)

        #Checkout
        if choice==5:
          if shopping_cart.is_empty():
            print("Your Shopping Cart is empty. Cannot proceed to checkout.")
          else:
            flag = shopping_cart.checkout()
            if flag:
              print("Thank you for shopping with Daily Seller. Have a great day!!")
              print("Exiting System....")
              break

        #Exit
        if choice==6:
          print("Thank you for shopping with Daily Seller. Have a great day!!")
          print("Exiting System....")
          break

    except ValueError:
        print("Enter the action in the requested format.")
