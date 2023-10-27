from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenRefreshView
from users.views import RegisterView, MyObtainTokenPairView

urlpatterns = [
    path("", include("core.urls")),
    path(
        "token/", MyObtainTokenPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),

    path('register/', RegisterView.as_view(), name='auth_register'),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
