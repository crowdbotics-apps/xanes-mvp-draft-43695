"""
WSGI config for xanes_mvp_draft_43695 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "xanes_mvp_draft_43695.settings"
)

application = get_wsgi_application()
