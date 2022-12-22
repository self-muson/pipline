from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .froms import *
from .models import *
from .utils import *



class WomenHome(DataMixin, ListView):
    
    model = Women
    template_name: str = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(contex.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')



# def index(request):
#     post = Women.objects.all()
    
#     context = {
#         'posts': post,
#         'title': 'Gлавная Cтраница!',
#         'cat_selected':0,
#     }
#     return render(request, 'women/index.html', context=context)
    
class WomenCategory(DataMixin, ListView):
    model = Women
    template_name: str = 'women/index.html'
    context_object_name: str = 'posts'
    allow_empty: bool = False


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])

        c_def = self.get_user_context(title='Категория - ' + str(c.name), cat_selected=c.pk)
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')
# def show_category(request, cat_id):
#     post = Women.objects.filter(cat_id=cat_id)
#     context = {
#         'posts': post,
#         'title': 'Otobrajenie po rubrikam!',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'women/index.html', context=context)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name: str = 'women/add_page.html'
    login_url: str = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить пост')
        return dict(list(context.items())+list(c_def.items()))

# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()

#     return render(request, 'women/add_page.html', {'form': form, 'menu': menu, 'title': 'Добавляем статью!'})



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items())+list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items())+list(c_def.items()))



# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)

#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'women/post.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'О проэкте!',})

class ContactUserView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')



# def contact(request):
#     return HttpResponse('Тут список контактов!')

def login(request):
    return HttpResponse('тут функционал добавления статей!!')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h>Нет такой страницы!</h1>')
