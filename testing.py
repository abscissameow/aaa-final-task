import pytest
from pizza import Pizza, Margherita, Pepperoni, Hawaiian


class TestPizza:
    def test_pizza_size(self):
        pizza = Pizza()
        assert pizza.size == 'L'

    def test_good_size(self):
        pizza = Pizza(size='XL')
        assert pizza.size == 'XL'

    def test_bad_size(self):
        with pytest.raises(TypeError):
            Pizza(size=27)

    def test_equal_pizzas(self):
        pizza1 = Margherita()
        pizza2 = Margherita(size='L')
        assert pizza1 == pizza2

    def test_different_pizzas(self):
        pizza1 = Hawaiian()
        pizza2 = Pepperoni()
        assert pizza1 != pizza2


if __name__ == '__main__':
    pytest.main()
