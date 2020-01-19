from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets

from rest_framework.permissions import IsAuthenticated
from iot.api.permissions import IsOwnerDevice

from iot.api.serializers import DeviceSerializer, UserInterfaceSerializer, RaspberryGpioSerializer
from iot.models import Device, UserInterface, RaspberryGpio

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

class CustomListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_kwarg_id(self): return self.kwargs.get("device_id")

    def get_queryset(self):
        return self.queryset.filter(device__id=self.get_kwarg_id())

    def perform_create(self, serializer):
        device = get_object_or_404(Device, id=self.get_kwarg_id())
        serializer.save(device=device)

class UserInterfaceListCreateAPIView(CustomListCreateAPIView):
    queryset = UserInterface.objects.all()
    serializer_class = UserInterfaceSerializer

class RaspberryGpioListCreateAPIView(CustomListCreateAPIView):
    queryset = RaspberryGpio.objects.all()
    serializer_class = RaspberryGpioSerializer

class UserInterfaceRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserInterface.objects.all()
    serializer_class = UserInterfaceSerializer
    permission_classes = [IsAuthenticated]#, IsOwnerDevice]

class RaspberryGpioRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RaspberryGpio.objects.all()
    serializer_class = RaspberryGpioSerializer
    permission_classes = [IsAuthenticated]#, IsOwnerDevice]
