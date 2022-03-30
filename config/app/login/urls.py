from django.urls import path, include
from app.login.views import *

urlpatterns = [
    path('', loginFormView2.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
