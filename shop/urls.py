from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('add/<int:product_id>',views.add_cart,name='addcart'),
    path('dec/<int:product_id>',views.min_cart,name='cart_decrement'),
    path('dele/<int:product_id>',views.cart_delete,name='remove'),
    path('cartdetails/', views.cart_details, name='cartDetails'),

    path('<slug:c_slug>/<slug:product_slug>',views.Details, name='details'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),

]