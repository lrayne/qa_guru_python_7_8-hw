class Product:
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity

    def buy(self, quantity: int = 1) -> None:
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    products: dict[Product, int]

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, buy_count: int = 1) -> None:
        if product not in self.products:
            self.products[product] = buy_count
        else:
            self.products[product] += buy_count

    def remove_product(self, product: Product, remove_count=None) -> None:
        if remove_count is None or remove_count > self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self) -> None:
        self.products.clear()

    def get_total_price(self) -> float:
        prices = [product.price * count for product, count in self.products.items()]
        return sum(prices)

    def buy(self) -> None:
        for product, count in self.products.items():
            if product.quantity >= count:
                product.quantity -= count
            else:
                raise ValueError
