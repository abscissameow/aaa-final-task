class Pizza:
    """
    мама-пицца
    """
    ingredients = None
    picture = None

    def __init__(self, size: str = 'L') -> None:
        if not isinstance(size, str):
            raise TypeError('размер - это строка')

        self.size = size

    def dict(self) -> dict:
        recipe = {self.__class__.__name__: self.ingredients}
        return recipe

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, self.__class__) and
            self.ingredients == other.ingredients and
            self.size == other.size
            )


class Margherita(Pizza):
    """
    хорошая дочка-пицца
    """
    ingredients = ['томатный соус', 'моцарелла', 'помидорки']
    picture = '🍅'


class Pepperoni(Pizza):
    """
    сыночек-пицца
    """
    ingredients = ['томатный соус', 'моцарелла', 'пепперони']
    picture = '🍕'


class Hawaiian(Pizza):
    """
    плохая дочка-пицца
    """
    ingredients = ['томатный соус', 'моцарелла', 'курочка', 'ананас']
    picture = '🍍'
