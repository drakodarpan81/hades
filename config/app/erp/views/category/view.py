from django.shortcuts import render
from app.erp.models import Category


def category_list(request):
    data = {
        'title': 'Listado de categorias',
        'icon': '<i class="fa-solid fa-list-check"></i>',
        'categorias': Category.objects.all()
    }
    return render(request, 'category/list.html', data)
