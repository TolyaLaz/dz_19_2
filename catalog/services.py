from django.core.cache import cache
from unicodedata import category

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_cached_list_categories():
    '''Получает данные по категориям из кэша, если кэш пуст-получает из бд'''
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = 'category_list'
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories