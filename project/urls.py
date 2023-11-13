
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as user_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('blog.urls')), #I put blog app at the root
    path('auth/', include('users.urls')),
    path('accounts/profile/', user_views.PasswordChangeView.as_view(), name="profile"),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
