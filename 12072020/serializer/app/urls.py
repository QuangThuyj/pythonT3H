from django.urls import path
from .views import *

urlpatterns = [
    path('hello', hello),
    path('get_product_list', getProductList),
    path('get_product_detail/<pk>', getProductDetail),
    path('create_product', createProduct),
    path('update_product/<pk>', updateProduct),
    path('update_product_partial/<pk>', updateProductPartial),
    path('delete_product/<pk>', deleteProduct)
]
