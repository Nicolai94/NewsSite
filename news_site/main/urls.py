from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import get_category, HomeNews, NewsByCategory, ViewNews, CreateNews, register, user_login, user_logout, contact

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>', get_category, name='category'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='category'),
    # path('news/<int:news_id>', view_news, name='view_news'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', add_news, name='add_news')
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
