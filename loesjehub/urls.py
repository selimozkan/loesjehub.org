from django.contrib import admin
from django.urls import path, include
from filebrowser.sites import site

urlpatterns = [
  path('admin/filebrowser/', site.urls),
  path('admin/', admin.site.urls),
  path('tinymce/', include('tinymce.urls')),
  path('', include('web.urls')),
]

