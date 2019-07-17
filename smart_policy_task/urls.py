from django.contrib import admin
from django.urls import include, path

from rest_auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    path('api/', include("main_app.api.urls")),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls'))
]
