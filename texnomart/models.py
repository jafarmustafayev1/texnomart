from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/products/', null=True, blank=True)
    is_primary = models.BooleanField(default=False)


class Comments(models.Model):
    class RatingChoices(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    body = models.TextField()
    rating = models.IntegerField(choices=RatingChoices.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment_product')
    bad_comment = models.TextField()
    good_comment = models.TextField()
    image = models.FileField(upload_to = Image, null=True, blank=True)
    rating 

