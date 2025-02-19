from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
  path('', views.HomeView.as_view(), name='index'),
  path('about/', views.AboutView.as_view(), name='about'),
  path('partners/', views.PartnersView.as_view(), name='partners'),
  path('projects/', views.ProjectsView.as_view(), name='projects'),
  path('resources/', views.ResourcesView.as_view(), name='resources'),
  path('contact/', views.ContactView.as_view(), name='contact'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)