from django.db import models
from django.conf import settings

class Device(models.Model):
    label = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="devices")
    def __str__(self):
        return self.label