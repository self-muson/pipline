from django.urls import path


from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactUserView.as_view(), name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', login, name='login'),
    path('posts/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', WomenCategory.as_view(), name='category')
    
   
    
    
]