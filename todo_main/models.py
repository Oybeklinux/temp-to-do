from email.mime import audio
from django.db import models

# Create your models here.


	# task char
	# is_completed bool def fal
	# cre auto_now_add
	# upd auto_now

class Tasks(models.Model):
    name = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
