from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe



class ProductImageInline(admin.TabularInline):
    model=ProductImage
    extra=1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'get_image')
    list_editable = ('category',)
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category__name')
    inlines = [
        ProductImageInline
    ]
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description="Rasmi")
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.get_image()}" width="150">')



admin.site.register([Category,ProductImage])