from django.db import models

# Create your models here.
class UrlDetails(models.Model):
    url = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.url)