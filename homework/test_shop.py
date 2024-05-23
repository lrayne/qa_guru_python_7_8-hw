import pytest
from homework.models import Product, Cart


@pytest.fixture
def cart():
    cart = Cart()
    return cart


@pytest.fixture
def not_empty_cart(cart, product):
    cart.add_product(product)
    return cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    def test_product_check_quantity(self, product):
        assert product.check_quantity(1000) == True
        assert product.check_quantity(999) == True
        assert product.check_quantity(1001) == False

    def test_product_buy(self, product):
        expected_quanity = product.quantity - 1
        product.buy(1)

        assert product.quantity == expected_quanity

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            assert product.buy(1001)
            assert product.buy(9999999)


class TestCart:
    def test_add_product_to_empty_cart(cart, product):
        cart.add_product(product)

        assert product in cart.products
        assert cart.products[product] == 1

    def test_add_same_product_to_not_empty_cart(cart, product):
        cart.add_product(product)
        cart.add_product(product)

        assert product in cart.products
        assert cart.products[product] == 2

    def test_add_product_quantity_to_empty_cart(cart, product):
        quantity = 20
        cart.add_product(product, buy_count=quantity)

        assert product in cart.products
        assert cart.products[product] == quantity

    def test_remove_product_from_cart(not_empty_cart, product):
        not_empty_cart.remove_product(product)

        assert not_empty_cart.products == {}

    def test_remove_product_count_from_cart(not_empty_cart, product):
        not_empty_cart.products[product] = 10
        not_empty_cart.remove_product(product, remove_count=5)

        assert not_empty_cart.products[product] == 5

    def test_remove_more_products_then_in_cart(not_empty_cart, product):
        not_empty_cart.remove_product(product, remove_count=100)

        assert not_empty_cart.products == {}

    def test_clear_cart(not_empty_cart):
        not_empty_cart.clear()
        assert not_empty_cart.products == {}

    def test_get_total_price(cart):
        phone = Product("phone", 10000, "This is a phone", 1000)
        pen = Product("pen", 200, "This is a pen", 3000)
        book = Product("book", 100, "This is a book", 1000)

        cart.add_product(phone)
        cart.add_product(pen)
        cart.add_product(book)

        assert cart.get_total_price() == 10300

    def test_buy_product(product):
        expected_quantity = product.quantity - 1
        product.buy()

        assert product.quantity == expected_quantity

    def test_buy_current_product_quantity(product):
        quantity = 100
        expected_quantity = product.quantity - quantity
        product.buy(quantity=100)

        assert product.quantity == expected_quantity

    def test_buy__product_quantity_more_than_avalibale(product):
        with pytest.raises(ValueError):
            assert product.buy(quantity=999999)
