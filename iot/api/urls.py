from django.urls import include, path
from iot.api import views as iv
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"devices", iv.DeviceViewSet)

urlpatterns = [
    path("", include(router.urls)),

]
