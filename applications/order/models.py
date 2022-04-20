from django.db import models

from applications.product.models import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    phone = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(null=True)

    def __str__(self):
        return self.phone
