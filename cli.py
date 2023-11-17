from pizza import Pizza, Margherita, Pepperoni, Hawaiian
from decorator import log
import click


@log('спасибо за заказ! приготовим твою пиццу за')
def bake(pizza: Pizza) -> None:
    """
    *готовится*
    """
    pass


@log('доставим твою пиццу за')
def deliever(pizza: Pizza) -> None:
    """
    *доставляется*
    """
    pass


def cli():
    pass


@log('ты сможешь забрать свою пиццу через')
def pickup(pizza: Pizza) -> None:
    """
    *самовывозится*
    """
    pass


@click.command()
def menu():
    """
    выводит меню пиццы
    """
    menu = {}
    menu['margherita'] = Margherita()
    menu['pepperoni'] = Pepperoni()
    menu['hawaiian'] = Hawaiian()

    for name, pizza in menu.items():
        ingredients = ', '.join(pizza.ingredients)
        print(f' • {name} {pizza.picture}: {ingredients}\n')


@click.command()
@click.option('--delivery', default=False, is_flag=True, help='флаг доставки')
@click.option('--size', default='L', help='размер пиццы (L/XL)')
@click.argument('pizza', nargs=1)
def order(delivery: bool, pizza: Pizza, size: str = None):
    """
    заказ!!
    """
    menus = {}
    menus["margherita"] = Margherita(size)
    menus["pepperoni"] = Pepperoni(size)
    menus["hawaiian"] = Hawaiian(size)
    if pizza not in menus:
        print("такой пиццы нет 🥺 выберем другую?")
        return
    if size and size not in {'L', 'XL'}:
        print('нет такого размера) L или XL? 😉')
        return
    bake(menus[pizza])
    if delivery:
        deliever(menus[pizza])
    else:
        pickup(menus[pizza])
        print('будем рады видеть тебя снова 🧡')


if __name__ == '__main__':
    clicker = click.Group()
    clicker.add_command(menu)
    clicker.add_command(order)
    clicker()
