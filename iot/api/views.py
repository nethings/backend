#from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets

from rest_framework.permissions import IsAuthenticated
from iot.api.permissions import IsOwnerDevice

from iot.api.serializers import DeviceSerializer
from iot.models import Device

#from iot.api.mixins import AllowPUTAsCreateMixin

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    lookup_field = "id"
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, IsOwnerDevice]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
