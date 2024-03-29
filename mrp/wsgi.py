"""
WSGI config for mrp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import time
import traceback
import signal
import sys



sys.path.append('/home/beng/mrp-system/emus-mrp')
sys.path.append('/home/beng/mrp-system/env/lib/python3.6/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mrp.settings.local")

#os.environ['HTTPS'] = "on"
from django.core.wsgi import get_wsgi_application
try: 
    application = get_wsgi_application() 
except Exception: 
    # Error loading applications 
    if 'mod_wsgi' in sys.modules: 
        traceback.print_exc() 
        os.kill(os.getpid(), signal.SIGINT) 
        time.sleep(2.5) 
        
