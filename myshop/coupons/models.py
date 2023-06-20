from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
   code = models.CharField(max_length=50, unique=True, verbose_name='Код купона')
   valid_from = models.DateTimeField(verbose_name='Действителен от')
   valid_to = models.DateTimeField(verbose_name='Действителен до')
   discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                              help_text=' Значение в процентах( от 0 to 100)',
                                              verbose_name='Скидка в %')
   active = models.BooleanField(verbose_name='Активность')
   
   def __str__(self):
     return self.code

