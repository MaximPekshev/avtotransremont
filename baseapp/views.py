from django.shortcuts import render, redirect
from baseapp.models import Category, Page, Staff
from django.shortcuts import get_object_or_404

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config
from .forms import ContactForm

def show_index_page(request):

    try:
        page = Page.objects.get(title__icontains='Главная')
    except:
        page = Page(title='Главная')
        page.save()

    context = {
        'categories' : Category.objects.filter(active=True),
        'categories_1': Category.objects.all()[:5],
        'categories_2': Category.objects.all()[5:10],
        'our_team': Staff.objects.all(),
        'page': page,
        'contact_form': ContactForm(),
    }

    return render(request, 'baseapp/index.html', context)

def show_category(request, cpu_slug):

    category = get_object_or_404(Category, cpu_slug=cpu_slug)
    
    context = {
        'categories': Category.objects.all(),
        'categories_1': Category.objects.all()[:5],
        'categories_2': Category.objects.all()[5:10],
        'category': category,
        'contact_form': ContactForm(),
    }

    return render(request, 'baseapp/category.html', context)

def show_contacts(request):

    try:
        page = Page.objects.get(title__icontains='Контакты')
    except:
        page = Page(title='Контакты')
        page.save()

    context = {
        'categories' : Category.objects.filter(active=True),
        'categories_1': Category.objects.all()[:5],
        'categories_2': Category.objects.all()[5:10],
        'page': page,
        'contact_form': ContactForm(),
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
        'categories_2': Category.objects.all()[5:10],
        'page': page,
        'contact_form': ContactForm(),
    }

    return render(request, 'baseapp/about.html', context)

def send_contact_form(request):

    if request.method == 'POST':
        
        contactForm = ContactForm(request.POST)
        
        if contactForm.is_valid():
            first_name = contactForm.cleaned_data['input_name']
            phone = contactForm.cleaned_data['input_phone']
            comment = contactForm.cleaned_data['input_comment']

            try:
                send_mail(first_name, phone, comment)
            except:
                return redirect('send_form_error')
            
            return redirect('send_form_success')
            
        else:
            
            return redirect('send_form_error')

def send_form_success(request):
    
    context = {
        'categories' : Category.objects.filter(active=True),
        'categories_1': Category.objects.all()[:5],
        'categories_2': Category.objects.all()[5:10],
        'contact_form': ContactForm(),
    }
    
    return render(request, 'baseapp/send_form_success.html', context)

def send_form_error(request):

    context = {
        'categories' : Category.objects.filter(active=True),
        'categories_1': Category.objects.all()[:5],
        'categories_2': Category.objects.all()[5:10],
        'contact_form': ContactForm(),
    }
    
    return render(request, 'baseapp/send_form_error.html', context)

def send_mail(first_name, phone, comment):

	HOST = "mail.hosting.reg.ru"
	sender_email = config('MAIL_USER')
	receiver_email = [config('MAIL_RECEIVER')]
	password = config('MAIL_PASSWORD')

	message = MIMEMultipart("alternative")
	message["Subject"] = "Свяжитесь с {}. Контакты: {} ".format(first_name, phone) 
	message["From"] = sender_email
	message["To"] = ','.join(receiver_email)

	text_body = """\
	"""

	html = """\
	<html>
      <body>
        <H3>Свяжитесь с {0}. Контакты: {1}</H3>
        <H3>Контакты:</H3>
        <p>Телефон: {1}</p>
        <p></p>
        <p>Комментарий:</p>
        <p>{2}</p>
      </body>
    </html>
	""".format(first_name, phone, comment)

	part1 = MIMEText(text_body, "plain")
	part2 = MIMEText(html, "html")
	message.attach(part1)
	message.attach(part2)

	context = ssl.create_default_context()

	server = smtplib.SMTP(HOST, 587)
	server.starttls()
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email , message.as_string())
	server.quit()