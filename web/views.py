from django.shortcuts import render
from django.views.generic import TemplateView

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
        context["latest_projects"] = Project.objects.all().order_by("-updated_at")[:3]
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
        try:
            context["header"] = PageHeader.objects.get(page="partners")
        except PageHeader.DoesNotExist:
            context["header"] = None
        context["partners"] = Partner.objects.all()
        return context


class ProjectsView(TemplateView):
    template_name = "projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = PageHeader.objects.get(page="projects")
        return context


class ProjectDetailView(TemplateView):
    template_name = "project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = PageHeader.objects.get(page="projects")
        context["project"] = Project.objects.get(slug=kwargs["slug"])
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
