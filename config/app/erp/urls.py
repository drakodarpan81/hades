from django.urls import path
from app.erp.views.category.view import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
]
