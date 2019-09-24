from modeltranslation.translator import register ,TranslationOptions
from .models import Category, Product 

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields=('name','description',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields=('slug',)