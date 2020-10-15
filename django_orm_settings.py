import django
from django.conf import settings

import os
import django

import orm_operations.settings
from orm_operations_app.models import *

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "orm_operations_app.settings"
)
django.setup()
