from django.db import models

# Create your models here.
class SavedText(models.Model):
    content = models.TextField(null=False, default='...', help_text='Copy some text here')
