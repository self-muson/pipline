from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('news/', index,),
    path('categories/<int:testid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

]