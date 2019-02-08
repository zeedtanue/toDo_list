from django.core.exceptions import ValidationError
from zipfile import ZipFile
#from django.utils.translation import gettext_lazy as _
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.zip']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
