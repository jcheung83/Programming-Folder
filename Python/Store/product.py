class Product:

    def __init__(self, name, price, category, id):
        self.name = name
        self.price = price
        self.category = category
        self.id = id

    def update_price(self, percent_change, is_increased):
        if (is_increased == True):
            self.price *= (1 + percent_change)
        elif (is_increased == False):
            self.price *= (1 - percent_change)
        return self
    
    def print_info(self):
        print("Name:", self.name)
        print(f"Price: {self.price:.2f}")
        print("Category", self.category)
        return self