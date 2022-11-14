import product

class Store:
    
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        for product.Product in self.products:
            if product.Product.id == id:
                print(f"Sold {product.Product.name} {product.Product.price:.2f} {product.Product.category}")
                self.products.remove(product.Product)
        return self

    def inflation(self, percent_increase):
        for product.Product in self.products:
            product.Product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product.Product in self.products:
            if product.Product.category == category:
                product.Product.update_price(percent_discount, False)
        return self

    def display_info(self):
        print("Name:", self.name)
        print("List of products: ")
        for i in range(len(self.products)):
            print(f"{self.products[i].name} {self.products[i].price:.2f} {self.products[i].category}")
        return self
