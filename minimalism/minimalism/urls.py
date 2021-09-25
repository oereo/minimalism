from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from feed.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name="landingPage"),
    path('accounts/', include('accounts.urls')),
    path('feed/', include('feed.urls')),
    path('diagnostic-test/', include('diagnostic_test.urls')),
    path('tagcloud/', include('tagcloud.urls')),
    path('pentagraph/', include('pentagraph.urls')),
    path('main/', include('main.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
