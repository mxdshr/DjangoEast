"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import xadmin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include

from werobot.contrib.django import make_view
from robot import robot


urlpatterns = [
    path('admin/', xadmin.site.urls,name="admin"),
    path('', include('blog.urls')),
    path('search/', include('haystack.urls')),
    path('mdeditor/', include('mdeditor.urls')),
    path('comment/', include('comment.urls')),
    path('robot/',make_view(robot)),
    path('notifications/', include('notifications.urls', namespace='notifications')),

]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # import debug_toolbar
    # urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
