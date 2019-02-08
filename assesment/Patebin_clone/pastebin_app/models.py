from django.db import models
from django.urls import reverse
from .utils import get_unique_slug

# Create your models here.

class Post(models.Model):
    name = models.CharField(db_index=True, max_length=300, blank=False)
    content = models.TextField()
    slug = models.SlugField(max_length=140, unique=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("pastebin_app:detail",kwargs={'slug':self.slug,
                                                'pk': self.pk})
