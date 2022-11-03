# Generated by Django 4.1.2 on 2022-10-17 10:18

import baseapp.models
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True, verbose_name='Заголовок')),
                ('meta_title', models.CharField(blank=True, max_length=150, null=True, verbose_name='meta title')),
                ('meta_description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='meta description')),
                ('meta_keywords', models.TextField(blank=True, max_length=1024, null=True, verbose_name='meta keywords')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', ckeditor.fields.RichTextField()),
                ('meta_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='meta name')),
                ('meta_keywords', models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='meta keywords')),
                ('meta_description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='meta description')),
                ('cpu_slug', models.SlugField(blank=True, max_length=70, verbose_name='ЧПУ_Url')),
                ('picture', models.ImageField(blank=True, default=None, null=True, upload_to=baseapp.models.get_image_name, verbose_name='Изображение 800x530')),
                ('parent_category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='baseapp.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
