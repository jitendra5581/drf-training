from django.db import models
from django.db.models.base import Model


class Blog(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.title