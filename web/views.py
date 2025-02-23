from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import (
    GeneralSetting,
    PageHeader,
    HomePage,
    About,
    Objective,
    SpecificObjective,
    Partner,
    Project,
    Resource,
    Contact,
)


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = HomePage.objects.first()
        context["objectives"] = Objective.objects.all()
        context["latest_projects"] = Project.objects.all().order_by(
            "-created_at", "-updated_at"
        )[:3]
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = PageHeader.objects.get(page="about")
        context["about"] = About.objects.first()
        context["objectives"] = Objective.objects.all()
        context["specific_objectives"] = SpecificObjective.objects.all()
        return context


class PartnersView(TemplateView):
    template_name = "partners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["header"] = PageHeader.objects.get(page="partners")
        except PageHeader.DoesNotExist:
            context["header"] = None
        context["partners"] = Partner.objects.all()
        return context


class ProjectsView(ListView):
    model = Project
    context_object_name = "projects"
    # paginate_by = 6
    template_name = "projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = PageHeader.objects.get(page="projects")
        return context


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = PageHeader.objects.get(page="projects")
        return context


class ResourcesView(TemplateView):
    template_name = "resources.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = PageHeader.objects.get(page="resources")
        context["resources"] = Resource.objects.all()
        return context


class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = PageHeader.objects.get(page="contact")
        context["contacts"] = Contact.objects.all()
        return context


class ImpressumView(TemplateView):
    template_name = "impressum.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["header"] = PageHeader.objects.get(page="impressum")
        except PageHeader.DoesNotExist:
            context["header"] = None
        context["impressum"] = HomePage.objects.filter().values_list(
            "impressum", flat=True
        )
        return context


class PrivacyPolicyView(TemplateView):
    template_name = "privacy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["header"] = PageHeader.objects.get(page="privacy")
        except PageHeader.DoesNotExist:
            context["header"] = None
        context["privacy"] = HomePage.objects.filter().values_list(
            "privacy_policy", flat=True
        )
        return context


class DisclaimerView(TemplateView):
    template_name = "disclaimer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["header"] = PageHeader.objects.get(page="disclaimer")
        except PageHeader.DoesNotExist:
            context["header"] = None
        context["disclaimer"] = HomePage.objects.filter().values_list(
            "disclaimer", flat=True
        )
        return context
