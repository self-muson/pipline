from django import template
from women.models import *
from women.views import menu

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.simple_tag()
def get_mainmenu():
    return menu


@register.simple_tag()
def get_posts(cat_id):
    
    return Women.objects.filter(cat_id=cat_id)
   
     



























# @register.inclusion_tag('women/list_mainmenu.html')
# def show_mainmenu(cat_id, filter=None):
    

#     if not filter:
#         posts = Women.objects.all()
#     else:
#         posts = Women.objects.filter(cat_id=cat_id)

#         context = {
#         'posts':posts,
#         'menu': menu,
#         'title': 'Otobrajenie po rubrikam!',
#         'cat_selected':cat_id,
#     }
#     return context