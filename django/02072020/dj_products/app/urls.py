from django.urls import path

from . import views_user, views_staff

urlpatterns = [
    path('', views_user.index, name='home'),
    path('product/<int:id>/', views_user.productDetail, name='productDetail'),
    path('add_to_cart/', views_user.addToCart, name='addToCart'),
    path('view_cart/', views_user.viewCart, name='viewCart'),
    path('update_cart_item/', views_user.updateCartItem, name='updateCartItem'),
    path('delete_cart_item/', views_user.deleteCartItem, name='deleteCartItem'),
    path('clear_cart/', views_user.clearCart, name='clearCart'),
    path('payment_info/', views_user.paymentInfo, name='paymentInfo'),
    path('confirm_payment/', views_user.confirmPayment, name='confirmPayment'),
    path('thankyou/', views_user.thankYou, name='thankYou'),
    path('contact/', views_user.contact, name='contact'),

    path('staff/', views_staff.listProduct, name='listProduct'),
    path('staff/add_product/', views_staff.addProduct, name='addProduct'),
    path('staff/edit_product/<int:id>/', views_staff.editProduct, name='editProduct'),
    path('staff/delete_product/<int:id>/', views_staff.deleteProduct, name='deleteProduct'),
]
