from datetime import datetime

class Order:
    def __init__(self, customer_name, hotel_name, items):
        self.customer_name = customer_name
        self.hotel_name = hotel_name
        self.items = items
        self.order_date = datetime.now()

    def total_amount(self):
        return sum(item.price for item in self.items)

    def __str__(self):
        return f"Order by {self.customer_name} at {self.hotel_name}"