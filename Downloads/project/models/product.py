class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category):
        self.category = new_category

    def edit_price(self, new_price):
        self.price = new_price

    def set_sale(self, sale):
        self.sale = sale

    def cancel_sale(self):
        self.sale = 0

    def get_price(self):
        # Это не тупо геттер - тут надо учесть скидку и еще то, что скидка указана в процентах
        return self.price * (1 - self.sale / 100)

    def __repr__(self):
        print('Product')
        print(f'Name: {self.name}')
        print(f'Category: {self.category}')
        print(f'Price: {self.price}')
        print(f'Final price: {self.get_price()}')
        print(f'Sale: {self.sale}')
        print()

