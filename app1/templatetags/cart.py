from django import template
from app1.models.category import Category
from app1.models.product import Product
from app1.models.orders import Order
register = template.Library()

@register.filter(name = 'is_in_cart')
def is_in_cart(id, cart):
    id = cart.get(str(id), False)
    if id:
        return True
    return False


@register.filter(name = 'qty_in_cart')
def qty_in_cart(id, cart):
    total = cart.get(str(id))
    return total
@register.filter(name = 'length_cart')
def qty_in_cart(cart):
    data = len(list(cart))
    return data

@register.filter(name = "add_currency")
def add_currenacy(price):
    return '₹ ' + str(price)

@register.filter(name = 'total_qty')
def total_qty(id, cart):
    qty = cart.get(str(id))
    return qty

@register.filter(name = 'total_price')
def total_price(id, cart):
    for x in cart:
        single_price = Product.objects.get(id = id).price
        qty = total_qty(id, cart)
        return single_price * qty
    
@register.filter(name = 'order_page_total_price')
def order_page_total_price(id):
    obj = Order.objects.get(id = id)
    single_price = obj.price
    qty = obj.qty
    return single_price * qty
    
@register.filter(name = 'final_price')
def final_price(cart):
    sum = 0
    print(cart)
    for x,y in cart.items():
        sum += total_price(x, cart)
    return sum


@register.filter(name = 'if_item_in_cart')
def if_item_in_cart(cart):
    data = len(list(cart))
    if data < 1:
        return False
    return True