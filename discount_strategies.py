from abc import ABC, abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, cart):
        pass

class PercentageOff(DiscountStrategy):
    def __init__(self, percentage):
      self.percentage = percentage

    def apply_discount(self, cart):
      total_price = sum(product.get_price() * quantity for product, quantity in cart.items())
      discount_amount = (self.percentage / 100) * total_price
      return total_price - discount_amount

    def get_strategy_name(self):
      return f"{self.percentage}% Off"

class BuyOneGetOneFree(DiscountStrategy):
    def apply_discount(self,cart):
      total_price=0
      for product, quantity in cart.items():
        if quantity >= 2:
          total_price += (quantity // 2) * product.get_price() + (quantity % 2) * product.get_price()
        else:
          total_price += product.get_price()
      return total_price

    def get_strategy_name(self):
        return "Buy One Get One Free"
