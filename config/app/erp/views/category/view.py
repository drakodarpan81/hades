from django.shortcuts import render
from app.erp.models import Category
from django.views.generic import ListView


def category_list(request):
    data = {
        'title': 'Listado de categorias',
        'icon': '<i class="fa-solid fa-list-check"></i>',
        'categorias': Category.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de categorias'
        return context


"""
# Muestra la información filtrada por la letra B
    def get_queryset(self):
        return Category.objects.filter(name__startswith='B')
"""
