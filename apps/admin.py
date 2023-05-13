from django.contrib import admin
from django.apps import apps
from django.utils.safestring import mark_safe
from apps.models import Product, Category, Person

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)

models = apps.get_app_config('apps').get_models()


@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name')
    list_display_links = ('name', 'get_image')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="200" height="200" />')
        return mark_safe('<p>No image</p>')


for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
