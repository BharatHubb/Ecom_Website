from django.shortcuts import render, HttpResponse, redirect
from app1.models.category import Category
from app1.models.product import Product
from app1.models.customer import Customer
from app1.models.orders import Order
from django.contrib.auth.hashers import make_password, check_password
from .middlewaer import login_one_required
# Create your views here.
def cart_details(request):
    id = request.POST.get('product')
    cart = request.session.get('cart')
    remove = request.POST.get('remove')
    qty = cart.get(id)
    if cart:
        if qty:
            if remove:
                if qty <= 1:
                    cart.pop(id)
                else:
                    cart[id] = qty - 1
            else:
                cart[id] = qty + 1
        else:
            cart[id] = 1
    else:
        cart = {}
        cart[id] = 1
    request.session['cart'] = cart



def index(request):
    if request.method == 'POST':
        cart_details(request)
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    return render(request, 'index.html', {'cat': Category.objects.all(), 'products': Product.objects.all()})

def cat(request, id):
    if request.method == 'POST':
        cart_details(request)
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    return render(request, 'index.html', {'cat': Category.objects.all(), 'products': Product.objects.filter(catogory_id = id)})

def cart(request):
    data = request.session.get('cart', None)
    if data:
        products = Product.objects.filter(id__in = list(data.keys()))
        return render(request, 'cart.html', {'products': products})
    return render(request, 'cart.html')

@login_one_required
def checkout(request):
    add = request.POST.get('address')
    phone = request.POST.get('phone')
    cart = request.session.get('cart')
    cust = request.session.get('id')
    products = Product.objects.filter(id__in = list(cart.keys()))
    lst_obj = []
    for x in products:
        qty = cart.get(str(x.id))
        price = x.price * qty
        obj = Order(product_id = x.id, customer_id = cust, price = price, qty = qty, address= add, phone = phone,)
        lst_obj.append(obj)
        cart.pop(str(x.id))
    Order.objects.bulk_create(lst_obj)
    request.session['cart'] = cart
    return redirect('order')


@login_one_required
def order(request):
    all = Order.objects.all()
    return render(request, 'orders.html', {'orders': all})

def sign_up(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = (request.POST.get('password'))
        password1 = (request.POST.get('password1'))
        error_message = None
        values = {
            'first_name': firstname,
            'last_name': lastname,
            'email': email,
            'phone': phone,
        }
        obj = Customer(first_name = firstname, last_name = lastname, email = email, phone = phone, password = make_password(password))
    
        if not(obj.first_name):
            error_message = "Please Enter your First Name !!"
        elif len(obj.first_name)<3:
            error_message = 'First Name must be 3 char long or more'
        elif not(obj.last_name):
            error_message = "Please Enter your Last Name !!"
        elif len(obj.last_name)<3:
            error_message = 'Last Name must be 3 char long or more'
        elif len (obj.email) < 5:
            error_message = 'Email must be 5 char long'
        elif len (password) < 5 :
            error_message = 'Password must be 5 char long'
        elif password != password1:
            error_message = "Password and Password1 must Same"
        elif (obj.phone):
            if len(obj.phone)<10:
                error_message = 'Phone Number must be 10 char Long'
            else:
                try:
                    obj2 = Customer.objects.get(phone = obj.phone)
                    if obj2:
                        raise ValueError
                except ValueError:
                    error_message = 'Phone Number Already Exits'
                except Customer.DoesNotExist:
                    pass
        if obj.email:
            if len(obj.email)<3:
                error_message = 'Email must be 3 char Long'
            else:
                try:
                    obj1 = Customer.objects.get(email = email)
                    if obj1:
                        raise ValueError
                except Customer.DoesNotExist:
                    pass
                except ValueError:
                    error_message = 'Email Address Already Registered..'
                    
        if not error_message:
            obj.save()
            msg = 'Sign Up Suessfully....'
            return render(request, 'signup.html', {'msg': msg})
        else:
            data = {
                'values': values, 
                'error' : error_message
            }
        return render(request, 'signup.html', data)
    return render(request, 'signup.html')
    

def log_in(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            obj = Customer.objects.get(email = email)
            valid_password = obj.password
            valid = check_password(password, valid_password)
            if valid:
                request.session['id'] = obj.id
                if request.POST.get('value'):
                    return redirect('cart')
                else:
                    return redirect('home')
            else:
                error = 'Invalid Credential'
                return render(request, 'login.html', {'error': error})
        except Customer.DoesNotExist:
                error = 'Invalid Credential'
                return render(request, 'login.html', {'error': error})           
    return render(request, 'login.html')


def log_out(request):
    request.session.pop('id')
    return redirect('log_in') 