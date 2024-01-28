from django.contrib import admin
from .models import Category

# Register your models here.
# @admin.register


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
