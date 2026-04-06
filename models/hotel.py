class Hotel:
    def __init__(self, hotel_id, name, location):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name} - {self.location}"