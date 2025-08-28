from modeltranslation import translator

from core.apps.products.models import Product


@translator.register(Product)
class ProductTranslation(translator.TranslationOptions):
    fields = [
        'name', 'description'
    ]