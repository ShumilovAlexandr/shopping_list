from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'image',
              'description', 'price',
              'quantity', 'created']
    list_display = ['name', 'show_photo',
                    'description', 'price',
                    'quantity', 'created']
    readonly_fields = ['created', 'show_photo']

    @admin.display(description='Изображение')
    def show_photo(self, obj: Product):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='60' "
                             f"height='50'>")
