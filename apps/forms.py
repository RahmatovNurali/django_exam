from django import forms
from .models import Product, Person, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'Person')


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'email')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
