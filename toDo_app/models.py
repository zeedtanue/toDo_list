from django.db import models
from .validator import validate_file_extension

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=50)

class Images(models.Model):
    image = models.FileField(upload_to ='uploads/', validators=[validate_file_extension])

    def __str__(self):
        return self.image
