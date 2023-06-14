from django.db import models
from shop.models import Product



class Order(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=64, verbose_name='Адрес')
    postal_code = models.CharField(max_length=16, verbose_name='Индекс')
    city = models.CharField(max_length=32, verbose_name='Регион')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Скорректирован')
    paid = models.BooleanField(default=False, verbose_name='Оплачен')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())   

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='Товар')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')


    def __str__(self):
        return str(self.id)
    

    def get_cost(self):
        return self.price * self.quantity

