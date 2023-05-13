from django.db import models
from django.db.models import ImageField


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    image = ImageField(upload_to='person_media', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
