from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category_detail'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('save_review/<int:product_id>/', save_review, name='save_review'),
    path('login_registration/', login_registration, name='login_registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('add_favourite/<slug:product_slug>/', save_favourite_product, name='add_favourite'),
    path('my_favourite/', FavouriteProductsView.as_view(), name='my_favourite'),
    path('cart/', cart, name='cart'),
    path('to_cart/<int:product_id>/<str:action>/', to_cart, name='to_cart'),
]


