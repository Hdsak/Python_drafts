from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import *
from .forms import *
from .utils import DataMixin


class WomenHome(DataMixin, ListView):
    paginate_by = 3
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Women, slug=self.kwargs['post_slug'])
        c_def = self.get_user_context(title='Главная страница', cat_selected=context['post'].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class WomanCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    template_name = 'women/add_page.html'
    form_class = AddPostForm
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


class About(DataMixin, ListView):
    template_name = 'women/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        c_def = self.get_user_context(title='О сайте')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return [1]


class RegisterUser(DataMixin, CreateView):
    template_name = 'women/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class ContactFormView(DataMixin, FormView):
    form_class = ContactUserForm
    template_name = 'women/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def contact(request):
    return HttpResponse('Обратная связь')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# def login(request):
#     return HttpResponse('Авторизация')


# def about(request):
#     return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})

# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/add_page.html', {'title': 'Добавление страницы', 'menu': menu, 'form': form})

# def index(request):
#     posts = Women.objects.all()
#     content = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': 0
#     }
#     return render(request, 'women/index.html', content)


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'women/post.html', context)


# def show_category(request, cat_slug):
#     # First method
#     # filter = Category.objects.filter(slug=cat_slug)
#     # posts = Women.objects.filter(cat = filter[0])
#     # Second Method
#     posts = Women.objects.filter(cat__slug=cat_slug)
#     if len(posts) == 0:
#         raise Http404()
#     content = {'title': 'Отображение по рубрикам', 'menu': menu, 'posts': posts, 'cat_selected': cat_slug}
#     return render(request, 'women/index.html', content)
#
