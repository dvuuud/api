from django.db import models

# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    banner_image = models.ImageField(upload_to='banners/', verbose_name='Фото')
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        
class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/', verbose_name='Фото')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты' 
           
           
