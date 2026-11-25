from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    model=Category
    list_display=['cname']

class ProductAdmin(admin.ModelAdmin):
    model=Product
    list_display=['category','pname','price','stock','is_available']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)