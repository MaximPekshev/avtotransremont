from django.contrib import admin

from .models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
	list_display = (
					'title',
					'cpu_slug',
					)
	
	exclude = ('cpu_slug', 'parent_category',)
	search_fields = ('title', )

admin.site.register(Category, CategoryAdmin)

admin.site.register(Page)