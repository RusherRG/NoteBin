from django.db import models

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=200, default="Example Note", help_text = 'Name of the note')
    user = models.CharField(max_length=100, default="Public", help_text = 'Who created this note? :(')
    time_modified = models.DateTimeField()
    note = models.TextField(default="Note", help_text = "The actual note")

class User(models.Model):
    # username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)