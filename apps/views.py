from django.shortcuts import render, redirect
from faker import Faker

from apps.forms import *


def index_view(request):
    return render(request, 'apps/index.html')


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_product')
    else:
        form = ProductForm()
    return render(request, 'apps/create_product.html', {'form': form})


def create_Person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_Person')
    else:
        form = PersonForm()
    return render(request, 'apps/create_Person.html', {'form': form})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_category')
    else:
        form = CategoryForm()
    return render(request, 'apps/create_category.html', {'form': form})


def faker_data(request):
    fake = Faker()
    objects = (Category(name=fake.name()) for i in range(100_000))
    Category.objects.bulk_create(objects)
    return redirect('index_view')
