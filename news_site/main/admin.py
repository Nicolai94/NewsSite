from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title', 'created_at',
                    'update_at', 'is_published', 'category', 'id', 'get_photo')
    list_display_links = ('title', 'id')
    search_fields = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'text', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'update_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'update_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
