from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Kategory nomi")


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="Tovar nomi", blank=False, null=False)
    description = models.TextField(verbose_name="Tovar haqida")
    price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name="Tovar narxi")
    discount_precent = models.PositiveSmallIntegerField(verbose_name="Chegirma foizi")
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)
    count = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def discount_price(self):
        return float(self.price) * (1 - self.discount_precent /100)


