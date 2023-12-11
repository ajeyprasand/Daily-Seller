# DAILY-SELLER
This repository contains python files which creates a simple E-commerce shopping system
Problem Statement
Functions can be performed:
1. Displaying listed products
2. Cart Functionality(made user-interactive):
         i)Add a product to cart
        ii)View current items in cart
       iii)Updating quantity of a product which exists in cart
        iv)Remove a product form cart
         v)Display the total bill
3. Discounts feature is present which can be modified during creation of cart object:
         i)Percentage off: This is applied to the total bill
         ii)Buy-One-Get-One free: This is applied on each product (depends on quantity of the product) 

Techniques used:
1.OOPs: Emphasize encapsulation and inheritance(base 'Product' class and subclasses for  textile_product,medicinal_product,electronic_product {note: for now no new attributes are added to the subclasses. But can be modified depending on the problem in hand like adding "expiry date" for mmedicinal_product classes})
2.Prototype design pattern: Instead of creating a new object to add it to the cart,the product in the product_registry is cloned
3.Strategy design pattern: This design pattern is used to implement discount features like buy-one-get-one-free and percentage offer

# To Run:
1. Clone the repo 
2. Run the Main program using any python compiler (Make sure to keep all the script files in same directory)

# Happy Shopping !!!
         
