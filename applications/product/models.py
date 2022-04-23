from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=35, primary_key=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.slug


User = get_user_model()


class Product(models.Model):
    CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии'),
    )
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    status = models.CharField(choices=CHOICES, max_length=20)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

class Rating(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='rating')
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='rating')
    rating = models.SmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ]

    )

class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like', verbose_name='владелец лайка')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='like', verbose_name='прщдукт')
    like = models.BooleanField('ЛАЙК', default=False)
    def __str__(self):
        return f'{self.owner}, {self.like}'

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.product)



