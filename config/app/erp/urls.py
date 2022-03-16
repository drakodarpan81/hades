from django.urls import path
from app.erp.views.category.view import category_list

app_name = 'erp'

urlpatterns = [
    path('category/list/', category_list, name='category_list'),
]
