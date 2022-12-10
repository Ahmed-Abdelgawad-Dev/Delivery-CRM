from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # My custom URLs
    path('', include('core.urls')),
    path('customers/', include('customers.urls')),
    path('items/', include('items.urls')),
    path('orders/', include('orders.urls')),
    # Third Party
    path('__debug__/', include('debug_toolbar.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
