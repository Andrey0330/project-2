from django import template
from women.models import Category

register = template.Library()

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


@register.simple_tag(name='get_category')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.sorted_by(sort)
    return {'categories': categories, 'cat_selected': cat_selected}


@register.simple_tag(name='menu')
def get_menu():
    return menu
