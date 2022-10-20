from django.urls import path
from .views import ProductList, ProductCreate, ProductDetail

urlpatterns = [
    path('', ProductList.as_view()),# to see the products
    path('create', ProductCreate.as_view()), #  to create the products
    path('<int:pk>', ProductDetail.as_view()), # to update and delete de products
]
