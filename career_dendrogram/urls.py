
# Updated 2 Code
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # Main application URLs
    path('accounts/', include('accounts.urls')),  # Accounts URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Default auth URLs (login, logout, password change, etc.)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
