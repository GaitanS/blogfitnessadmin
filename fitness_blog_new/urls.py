"""
URL configuration for fitness_blog_new project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Import include
from django.conf import settings             # Import settings
from django.conf.urls.static import static     # Import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # Include blog app urls
]

# Add static and media file serving patterns for development (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Although runserver handles this, it's good practice
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
