# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1816396/data/www/avtotransremont.ru/autotransremont')
sys.path.insert(1, '/var/www/u1816396/data/www/avtotransremont.ru/venv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'autotransremont.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()