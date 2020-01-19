from django.contrib import admin
from iot.models import Device, UserInterface, RaspberryGpio

admin.site.register(Device)
admin.site.register(UserInterface)
admin.site.register(RaspberryGpio)