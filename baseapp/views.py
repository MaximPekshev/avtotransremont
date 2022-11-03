from django.shortcuts import render
from baseapp.models import Category, Page
from django.shortcuts import get_object_or_404

def show_index_page(request):

    try:
        page = Page.objects.get(title__icontains='Главная')
    except:
        page = Page(title='Главная')
        page.save()

    context = {
        'categories' : Category.objects.filter(active=True),
        'categories_1': Category.objects.all()[:5],
        'categories_2': Category.objects.all()[6:],
        'page': page,
    }

    return render(request, 'baseapp/index.html', context)

def show_category(request, cpu_slug):

    category = get_object_or_404(Category, cpu_slug=cpu_slug)
    template_name = category.cpu_slug + '.html'

    context = {
        'categories': Category.objects.all(),
        'categories_1': Category.objects.all()[:5],
        'categories_2': Category.objects.all()[6:],
        'category': category,
    }

    return render(request, 'baseapp/category/' + template_name, context)

def show_contacts(request):

    try:
        page = Page.objects.get(title__icontains='Контакты')
    except:
        page = Page(title='Контакты')
        page.save()

    context = {
        'categories' : Category.objects.filter(active=True),
        'categories_1': Category.objects.all()[:5],
        'categories_2': Category.objects.all()[6:],
        'page': page,
    }

    return render(request, 'baseapp/contacts.html', context)

def show_about_us(request):

    try:
        page = Page.objects.get(title__icontains='О нас')
    except:
        page = Page(title='О нас')
        page.save()


    context = {
        'categories' : Category.objects.filter(active=True),
        'categories_1': Category.objects.all()[:5],
        'categories_2': Category.objects.all()[6:],
        'page': page,
    }

    return render(request, 'baseapp/about.html', context)    