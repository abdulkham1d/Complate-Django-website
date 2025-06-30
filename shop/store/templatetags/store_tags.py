from django import template
from store.models import *

register = template.Library()


# Otasi borlarini olib chiqadi !
@register.simple_tag()
def get_categories():
    return Category.objects.filter(parent=True)


@register.simple_tag()
def get_categories_s():
    return Category.objects.filter(parent=None)


# Yetim kategoriyaga tegishli kategoriyalani beradi !!!
@register.simple_tag()
def get_subcategories(category):
    return Category.objects.filter(parent=category)



@register.simple_tag()
def get_sorted():
    sorters = [
        {
            'title': 'Price',
            'sorters': [
                ('price', 'Cheap'),
                ('-price', 'Expensive')
            ]
        },
        {
            'title': 'Metal',
            'sorters': [
                ('metal_product', 'A - Z'),
                ('-metal_product', 'Z - A')
            ]
        },
        {
            'title': 'Size',
            'sorters': [
                ('size', 'Small size'),
                ('-size', 'Big size')
            ]
        },
    ]
    return sorters


@register.simple_tag()
def get_favourite_products(user):
    fav = FavouriteProducts.objects.filter(user=user)
    products = [i.product for i in fav]
    return products