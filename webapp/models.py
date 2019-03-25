from django.db import models

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=200, help_text = 'Name of the note')
    time_created = models.DateTimeField()
    time_modified = models.DateTimeField()
    note = models.TextField()