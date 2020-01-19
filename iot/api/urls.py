from django.urls import include, path
from iot.api import views as v
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"devices", v.DeviceViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path("devices/<int:device_id>/ui/",
      v.UserInterfaceListCreateAPIView.as_view(),
      name="device-ui"),

    path("devices/<int:device_id>/gpio/",
      v.RaspberryGpioListCreateAPIView.as_view(),
      name="device-gpio"),

    path("ui/<int:pk>/",
      v.UserInterfaceRUDAPIView.as_view(),
      name="ui"),

    path("gpio/<int:pk>/",
      v.RaspberryGpioRUDAPIView.as_view(),
      name="gpio"),
]
