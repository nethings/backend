from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login tramite browsable API
    path('api-auth/',
        include("rest_framework.urls")),

    # Login tramite REST API
    path('api/rest-auth/',
        include("rest_auth.urls")),

]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns.append(re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"))
