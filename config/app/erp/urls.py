from django.urls import path
from app.erp.views.category.view import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
    path('category/update/<int:pk>',
         CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>',
         CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
]
