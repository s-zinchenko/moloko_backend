# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/z/zinchi5d/zinchi5d.beget.tech/moloko_backend')
sys.path.insert(1, '/home/z/zinchi5d/zinchi5d.beget.tech/moloko_backend/venv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'moloko_backend.application.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()