from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="kategoriya nomi")



class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="tovar nomi")
    description = models.TextField( verbose_name="tovar haqida")
    price = models.IntegerField(verbose_name="tovar narxi")
    discount_precent = models.PositiveSmallIntegerField(verbose_name="chegirma foizi")
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    count = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



