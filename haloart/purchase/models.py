from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название продукта')
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    description = models.TextField(verbose_name='Описание продукта')
    price = models.DecimalField(
        verbose_name='Цена продукта',
        decimal_places=2,
        max_digits=7
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(limit_value=1,
                                      message='Минимальное количество '
                                              'товара не может быть меньше '
                                              '1')],
        verbose_name='Количество единиц товара')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата добавления товара в')

    class Meta:
        ordering = ['price']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('new_product')



