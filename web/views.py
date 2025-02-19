from django.shortcuts import render
from django.views.generic import TemplateView

from .models import GeneralSetting, PageHeader, HomePage, About, Objective, SpecificObjective, Partner, Project, Resource, Contact

class HomeView(TemplateView):
  template_name = "index.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["home"] = HomePage.objects.first()
    context["objectives"] = Objective.objects.all()
    return context

class AboutView(TemplateView):
  template_name = "about.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["header"] = PageHeader.objects.get(page="about")
    return context
  
class PartnersView(TemplateView):
  template_name = "partners.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["header"] = PageHeader.objects.get(page="partners")
    return context

class ProjectsView(TemplateView):
  template_name = "projects.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["header"] = PageHeader.objects.get(page="projects")
    return context

class ResourcesView(TemplateView):
  template_name = "resources.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["header"] = PageHeader.objects.get(page="resources")
    return context

class ContactView(TemplateView):
  template_name = "contact.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["header"] = PageHeader.objects.get(page="contact")
    return context
