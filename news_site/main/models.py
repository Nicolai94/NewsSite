from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank='True')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})
