from django.shortcuts import (render,
                              redirect)
from django.views.generic.edit import (CreateView,
                                       UpdateView,
                                       DeleteView)
from django.views.generic.base import TemplateView

from django.urls import (reverse_lazy,
                         reverse)
from django.http import HttpResponse, JsonResponse

from .models import Product
from .forms import AddProductForm
from django.http import JsonResponse
from django.template.loader import render_to_string


class MainTitleView(TemplateView):
    """Класс для отображения главной страницы со списком продуктов."""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        obj_sort = self.request.GET.get('object_sort')
        name_filter = self.request.GET.get('name_filter')

        all_objects = Product.objects.all()

        # Фильтрация по названию
        if name_filter:
            all_objects = all_objects.filter(name__icontains=name_filter)

        # Сортировка
        if obj_sort:
            if obj_sort == 'Название':
                all_objects = all_objects.order_by('name')
            elif obj_sort == 'Цена':
                all_objects = all_objects.order_by('price')
            elif obj_sort == 'Количество':
                all_objects = all_objects.order_by('quantity')
            elif obj_sort == 'Дата добавления':
                all_objects = all_objects.order_by('created')

        context['instance'] = all_objects
        return context


class AddNewProductView(CreateView):
    """Класс для создания нового продукта."""
    template_name = 'new_product.html'
    form_class = AddProductForm
    extra_context = {
        'title': 'Создание нового продукта'
    }


class UpdateProductView(UpdateView):
    model = Product
    fields = ['name', 'image', 'description', 'price', 'quantity']
    template_name = 'new_product.html'
    success_url = reverse_lazy('main_page')
    extra_context = {
        'title': 'Редактирование продукта'
    }


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('main_page')
    extra_context = {
        'title': 'Удаление продукта'
    }





