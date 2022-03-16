from django.urls import path

from app.erp.views import Home, Index

app_name = 'erp'

urlpatterns = [
    path('', Home, name='home'),
    path('index/', Index, name='index'),
]
