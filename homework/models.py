class Product:
    """
    Класс продукта
    """

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
        return True if self.quantity >= quantity else False

    def buy(self, quantity: int = 1) -> None:
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count: int = 1) -> None:
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product not in self.products:
            self.products[product] = buy_count
        else:
            self.products[product] += buy_count

    def remove_product(self, product: Product, remove_count=None) -> None:
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None or remove_count > self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self) -> None:
        self.products.clear()

    def get_total_price(self) -> float:
        prices = [product.price for product in self.products.keys()]

        return sum(prices)

    def buy(self, product: Product, buy_count: int = 1) -> None:
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        if product.quantity >= buy_count:
            product.quantity -= buy_count
        else:
            raise ValueError
