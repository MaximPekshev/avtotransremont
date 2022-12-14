# Generated by Django 4.1.2 on 2022-11-02 14:53

import baseapp.models
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_alter_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Активная страница'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=baseapp.models.get_image_name, verbose_name='Изображение 870x349'),
        ),
    ]
