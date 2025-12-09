import sys
import os

# 1. Add the current directory to the Python path
# This ensures Python can find the top-level folder, which contains the '_base' folder.
sys.path.insert(0, os.getcwd())

# 2. CONFIGURE DJANGO SETTINGS (CRITICAL CHANGE)
# The actual Django project module is named '_base'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_base.settings')

# 3. Get the WSGI application object
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()