from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from .models import News, Category
from .utils import MyMixin


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'main/home_news_list.html'
    context_object_name = 'news'
    # mixin_prop = 'Hello world'
    paginate_by = 3

    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная старница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def index(request):
##context = {
#    'news': news,
#  'title': 'Список новостей',
# }
# return render(request, 'main/index.html', context)

class NewsByCategory(ListView):
    model = News
    template_name = 'main/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 3

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'news': news, 'category': category}
    return render(request, 'main/category.html', context)


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # template_name = 'news/news_detail.html'
    # pk_url_kwarg = 'news_id'


# def view_news(request, news_id):
# news_item = News.objects.get(pk=news_id)
# news_item = get_object_or_404(News, pk=news_id)
# context = {'news_item': news_item}
# return render(request, 'main/view_news.html', context)

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'main/add_news.html'
    # login_url = '/admin/'
    raise_exception = True
    # success_url = reverse_lazy('home')


# def add_news(request):
#   if request.method == 'POST':
#      form = NewsForm(request.POST)
#     if form.is_valid():
#        # print(form.cleaned_data)
#       # news = News.objects.create(**form.cleaned_data)
#      news = form.save()
#     return redirect(news)
# else:
#   form = NewsForm()
# return render(request, 'main/add_news.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
    else:
        form = UserRegisterForm()
        messages.error(request, 'Ошибка регистрации')
    context = {'form': form}
    return render(request, 'main/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'main/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'nick94@bk.ru',
                             ['nicolas9441@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'main/contact.html', context)
