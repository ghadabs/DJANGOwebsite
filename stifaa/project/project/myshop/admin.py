from django.contrib import admin
from .models import Category, Product
from modeltranslation.translator import translator, TranslationOptions

# class SubcategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}
# admin.site.register(Subcategory,SubcategoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'subcategory',
                    'price', 'brand_photo', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created',
                   'updated', 'category', 'subcategory']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)

class ProductTranslationOptions(TranslationOptions):
    fields = ('name','description',)

translator.register(Product, ProductTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('slug',)

translator.register(Category, CategoryTranslationOptions)