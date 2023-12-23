from django.contrib import admin

from catalog.models import Product, Category, BlogNotes, VersionProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_category',)
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)

@admin.register(BlogNotes)
class BlogNotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active',)

@admin.register(VersionProduct)
class VersionProductAdmin(admin.ModelAdmin):
    pass

