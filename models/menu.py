class MenuItem:
    def __init__(self, item_id, hotel_id, name, price):
        self.item_id = item_id
        self.hotel_id = hotel_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (₹{self.price})"