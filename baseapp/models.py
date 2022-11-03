from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

import uuid
from uuslug import slugify
import os

def get_image_name(instance, filename):
	
	new_name = ('%s' + '.' + filename.split('.')[-1]) % instance.cpu_slug
	return new_name

def get_image_title_name(instance, filename):
	
	new_name = ('%s' + '.' + filename.split('.')[-1]) % instance.title
	return new_name

class Category(models.Model):
    
    title 				= models.CharField(max_length = 150, verbose_name='Наименование')
    description 		= RichTextUploadingField(verbose_name='Описание', blank=True, null=True)
    meta_name 			= models.CharField(max_length=150, verbose_name='meta name', blank=True, null=True)
    meta_keywords 		= models.CharField(max_length=150, verbose_name='meta keywords', blank=True, null=True, default="")
    meta_description 	= models.TextField(max_length=1024, verbose_name='meta description', blank=True, null=True)
    cpu_slug			= models.SlugField(max_length=70, verbose_name='ЧПУ_Url', blank=True, db_index=True)
    picture				= models.ImageField(upload_to=get_image_name, verbose_name='Изображение 870x349', default=None, null=True, blank=True)
    parent_category 	= models.ForeignKey('Category', verbose_name='Категория', on_delete=models.SET_DEFAULT,null=True, blank=True, default=None)
    active              = models.BooleanField(verbose_name='Активная страница', default=False)    
    
    def __str__(self):
        
        return self.title
        
    def save(self, *args, **kwargs):
        
        self.cpu_slug = '{}'.format(slugify(self.title))
        if not os.path.exists('baseapp/templates/baseapp/category/' + self.cpu_slug + '.html'):
            file_name = 'baseapp/templates/baseapp/category/' + self.cpu_slug + '.html'
            file_content = """
{% extends 'baseapp/category/base_category.html' %}

{% load static %}

{% block title %}{% if category.meta_name %}{{ category.meta_name }}{% else %}{% endif %}{% endblock %}
{% block keywords %}{% if category.meta_keywords %}{{ category.meta_keywords }}{% else %}{% endif %}{% endblock %}
{% block description %}{% if category.meta_description %}{{ category.meta_description }}{% else %}{% endif %}{% endblock %}

{% block category_content %}
<div class="row clearfix">
    <section class="left-content col-lg-12 col-md-12 col-sm-12 col-xs-12">
        <article class="post post-detail">
            <div class="post-image wow fadeInUp" data-wow-delay="200ms" data-wow-duration="1500ms">
                <img class="img-responsive" src="{% if category.picture %}{{ category.picture.url }}{% endif %}" alt="">
            </div>
            {% if category.description %}
            <div class="content-box">
                <div class="post-data">
                    {{ category.description|safe  }}
                </div>
            </div>
            {% endif %}
        </article>
    </section>
</div>
{% endblock %}

{% block content %}
{{ block.super }}
{% endblock %}
            """
            category_file = open(file_name, "+w")
            category_file.write(file_content)
            category_file.close()
        super(Category, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        template = os.path.exists('baseapp/templates/baseapp/category/' + self.cpu_slug + '.html')
        if template:
            os.remove('baseapp/templates/baseapp/category/' + self.cpu_slug + '.html')
        super(Category, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Page(models.Model):

	title 				= models.CharField(max_length=150, verbose_name="Заголовок", null=True)
	meta_title 			= models.CharField(max_length=150, verbose_name='meta title', blank=True, null=True)
	meta_description 	= models.TextField(max_length=1024, verbose_name='meta description', blank=True, null=True)
	meta_keywords 		= models.TextField(max_length=1024, verbose_name='meta keywords', blank=True, null=True)
		
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Страница'
		verbose_name_plural = 'Страницы'
