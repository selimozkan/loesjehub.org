from django.contrib import admin
from django.contrib.auth.models import Group

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


class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ("website_title", "website_description", "website_keywords")
    fields = ("website_title", "website_description", "website_keywords")

    def has_add_permission(self, request):
        return not GeneralSetting.objects.exists()


class PageHeaderAdmin(admin.ModelAdmin):
    list_display = ["bg_thumbnail", "page", "page_title", "page_description"]
    list_display_links = ["bg_thumbnail", "page", "page_title"]
    fields = ["bg_image", "page_image", "page", "page_title", "page_description"]
    readonly_fields = [
        "bg_image",
    ]

    def has_add_permission(self, request):
        count = PageHeader.objects.all().count()
        return count <= 7


class HomePageAdmin(admin.ModelAdmin):
    list_display = ["thumb", "welcome_title", "latest_projects_title"]
    list_display_links = [
        "thumb",
        "welcome_title",
    ]
    fields = [
        "img",
        "welcome_image",
        "welcome_title",
        "welcome_description",
        "objectives_img",
        "objectives_image",
        "objectives_title",
        "latest_projects_title",
        "latest_projects_description",
        "impressum",
        "privacy_policy",
        "disclaimer",
    ]
    readonly_fields = [
        "img",
        "objectives_img",
    ]

    def has_add_permission(self, request):
        return not HomePage.objects.exists()


class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    fields = ["title", "description"]

    def has_add_permission(self, request):
        count = Objective.objects.all().count()
        return count <= 4


class SpecificObjectiveAdmin(admin.ModelAdmin):
    list_display = ["objective", "title", "description"]
    fields = ["objective", "title", "description"]

    def has_add_permission(self, request):
        count = SpecificObjective.objects.all().count()
        return count <= 3


class AboutAdmin(admin.ModelAdmin):
    list_display = ["thumb", "description"]
    list_display_links = ("thumb", "description")
    fields = ["img", "image", "description"]
    readonly_fields = [
        "img",
    ]

    def has_add_permission(self, request):
        return not About.objects.exists()


class PartnerAdmin(admin.ModelAdmin):
    list_display = ["thumb", "name", "short_description", "linktree"]
    list_display_links = ("thumb", "name")
    fields = [
        "img",
        "image",
        "name",
        "short_description",
        "long_description",
        "linktree",
    ]
    readonly_fields = [
        "img",
    ]

    def has_add_permission(self, request):
        count = Partner.objects.all().count()
        return count <= 4


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["thumb", "author", "title", "ongoing", "created_at", "updated_at"]
    list_display_links = ("thumb", "author", "title")
    fields = [
        "img",
        "image",
        "author",
        "partners",
        "title",
        "description",
        "article",
        "ongoing",
        "slug",
    ]
    readonly_fields = [
        "img",
    ]
    prepopulated_fields = {"slug": ("title",)}


class ResourceAdmin(admin.ModelAdmin):
    list_display = ["thumb", "title", "link"]
    list_display_links = ("thumb", "title")
    fields = ["img", "image", "title", "description", "link"]
    readonly_fields = [
        "img",
    ]


class ContactAdmin(admin.ModelAdmin):
    list_display = ["thumb", "title", "phone", "email", "linktree"]
    list_display_links = ("thumb", "title")
    fields = ["img", "image", "title", "phone", "address", "email", "linktree"]
    readonly_fields = [
        "img",
    ]

    def has_add_permission(self, request):
        count = Contact.objects.all().count()
        return count <= 4


admin.site.register(GeneralSetting, GeneralSettingAdmin)
admin.site.register(PageHeader, PageHeaderAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(SpecificObjective, SpecificObjectiveAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Contact, ContactAdmin)


admin.site.unregister(Group)

admin.site.site_header = "LoesjeHub Admin Panel"
admin.site.site_title = "LoesjeHub Admin Panel"
