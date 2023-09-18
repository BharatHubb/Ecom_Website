from django.urls import path
from .views import *




urlpatterns = [
    path('home/', index, name = 'home'),
    path('cat/<int:id>/', cat, name = 'cat'),
    path('cart/', cart, name = 'cart'),
    path('order/', order, name = 'order'),
    path('checkout/', checkout, name = 'checkout'),
    path('signup/', sign_up, name = 'sign_up'),
    path('login/', log_in, name = 'log_in'),
    path('logout/', log_out, name = 'logout'),
]






