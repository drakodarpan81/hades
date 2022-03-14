from django.urls import path

from app.erp.views import myfirstview, mysecondview

urlpatterns = [
    path('primera/', myfirstview),
    path('segunda/', mysecondview),
]
