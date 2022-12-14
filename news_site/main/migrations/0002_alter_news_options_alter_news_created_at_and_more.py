# Generated by Django 4.0.6 on 2022-07-31 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank='True', upload_to='photos/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлен'),
        ),
    ]
