from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Device(models.Model):
    label = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="devices")
    def __str__(self):
        return self.label

class UserInterface(models.Model):
    FIELDS = (("text", "Text"),("switch", "Switch"),("slider", "Slider"))
    field = models.CharField(max_length=24, choices=FIELDS)
    prefix = models.CharField(max_length=10, default="", blank=True)
    suffix = models.CharField(max_length=10, default="", blank=True)
    min = models.IntegerField(blank=True, null=True)
    max = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=50, blank=True)
    device = models.ForeignKey(Device, related_name="uis",
                            on_delete=models.CASCADE)

    def __str__(self):
        return self.label

class RaspberryGpio(models.Model):
    DIRECTIONS = ((1, "Input"),(0, "Output"))
    direction = models.IntegerField(choices=DIRECTIONS)
    address = models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(27)])
    label = models.CharField(max_length=50, blank=True)
    device = models.ForeignKey(Device, related_name="gpios",
                            on_delete=models.CASCADE)

    def __str__(self):
        return self.label