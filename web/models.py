from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone
import random

from tinymce.models import HTMLField
from multiselectfield import MultiSelectField

PARTNER_CHOICES = (
  ('berlin', 'Loesje Berlin')  ,
  ('bulgaria', 'Loesje Bulgaria'),
  ('bitola', 'Loesje Bitola'),
  ('gnu', 'GNU'),
)
PROJECT_STATUS_CHOICES = (
  ('ongoing', 'Ongoing'),
  ('past', 'Past')
)

PAGE_CHOICES = (
  ('about', 'ABOUT THE PROJECT'),
  ('partners', 'PARTNERS'),
  ('projects', 'PROJECTS'),
  ('resources', 'RESOURCES'),
  ('contact', 'CONTACT'),
)

def create_slug(title):
  slug = slugify(title)
  if Project.objects.filter(slug=slug).exists():
    slug = "%s-%d" % (slug, random.randint(1,99999))
  return slug


class GeneralSetting(models.Model):
  website_title = models.CharField(max_length=250, null=True, blank=True)
  website_description = models.TextField(null=True, blank=True)
  website_keywords = models.CharField(max_length=250, null=True, blank=True)

  class Meta:
    verbose_name = 'General Setting'
    verbose_name_plural = 'General Settings'
    managed = True
    ordering = ('id',)

  def __str__(self):
    return self.website_title

class PageHeader(models.Model):
  page = models.CharField("Related Page", max_length=25, choices=PAGE_CHOICES, null=False, blank=False, default="about")
  page_image = models.ImageField(upload_to='pageheaders/',validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg", "jpeg"])],)
  page_title = models.CharField(max_length=75, null=True, blank=True)
  page_description = models.TextField(null=True, blank=True)

  class Meta: 
    verbose_name = 'Page Header'
    verbose_name_plural = 'Page Headers'
    managed = True
    ordering = ('id',)

  def bg_thumbnail(self):
    if self.page_image:
      return mark_safe('<img src="%s" style="width:50px;height:50px;" alt="" />' % self.page_image.url)
    else:
      return "No Image"
    bg_thumbnail.short_description = 'Page Image'
    bg_thumbnail.allow_tags = True

  def bg_image(self):
    if self.page_image:
      return mark_safe('<img src="%s" style="height:150px;" alt="" />' % self.page_image.url)
    else:
      return "No Image"
    bg_image.short_description = 'Page Image'
    bg_image.allow_tags = True

  def __str__(self):
    return self.page_title

class HomePage(models.Model):
  welcome_image = models.ImageField(upload_to='home/',validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg", "jpeg"])])
  welcome_title = models.CharField(max_length=75, null=True, blank=True)
  welcome_description = models.TextField(null=True, blank=True)
  objectives_title = models.CharField(max_length=50, null=True, blank=True)
  objectives_image = models.ImageField(upload_to='home/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg", "jpeg"])])
  latest_projects_title = models.CharField(max_length=75, null=True, blank=True)
  latest_projects_description = models.TextField(null=True, blank=True)
  impressum = HTMLField(null=True, blank=True)
  privacy_policy = HTMLField(null=True, blank=True)
  disclaimer = HTMLField(null=True, blank=True)

  class Meta:
    verbose_name = 'Home'
    verbose_name_plural = 'Home Items'
    managed = True

  def __str__(self):
    return self.welcome_title

  def thumb(self):
    if self.welcome_image:
      return mark_safe('<img src="%s" style="width:50px;height:50px;" alt="" />' % self.welcome_image.url)
    else:
      return "No Image"
    thumb.short_description = 'Welcome Image'
    thumb.allow_tags = True

  def img(self):
    if self.welcome_image:
      return mark_safe('<img src="%s" style="height:150px;" alt="" />' % self.welcome_image.url)
    else:
      return "No Image"
    img.short_description = 'Welcome Image'
    img.allow_tags = True

  def objectives_img(self):
    if self.objectives_image:
      return mark_safe('<img src="%s" style="height:150px;" alt="" />' % self.objectives_image.url)
    else:
      return "No Image"
    img.short_description = 'Objectives Image'
    img.allow_tags = True


class Objective(models.Model):
  title = models.CharField(max_length=50, null=True, blank=True)
  description = models.TextField(null=True, blank=True)

  class Meta:
    verbose_name = 'Objective'
    verbose_name_plural = 'Objectives'
    managed = True
    ordering = ('id',)

  def __str__(self):
    return self.title

class SpecificObjective(models.Model):
  objective = models.ForeignKey(Objective, on_delete=models.CASCADE, null=False, blank=False)
  title = models.CharField(max_length=75, null=True, blank=True)
  description = models.TextField(null=True, blank=True)

  class Meta:
    verbose_name = 'Specific Objective'
    verbose_name_plural = 'Specific Objectives'
    managed = True
    ordering = ('id',)

  def __str__(self):
    return self.title

class About(models.Model):
  image = models.ImageField(upload_to='about/',validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg", "jpeg"])])
  description = HTMLField(null=True, blank=True)

  class Meta:
    verbose_name = 'About'
    verbose_name_plural = 'About'
    managed = True
    ordering = ('id',)

  def __str__(self):
    return self.description

  def thumb(self):
    if self.image:
      return mark_safe('<img src="%s" style="width:50px;height:50px;" alt="" />' % self.image.url)
    else:
      return "No Image"
    thumb.short_description = 'About Image'
    thumb.allow_tags = True

  def img(self):
    if self.image:
      return mark_safe('<img src="%s" style="height:150px;" alt="" />' % self.image.url)
    else:
      return "No Image"
    img.short_description = 'About Image'
    img.allow_tags = True

class Partner(models.Model):
  image = models.ImageField(upload_to='partner/',validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg", "jpeg"])])
  name = models.CharField(max_length=100, null=True, blank=True)
  short_description = models.TextField(null=True, blank=True)
  long_description = HTMLField(null=True, blank=True)
  linktree = models.URLField(null=True, blank=True)

  class Meta:
    verbose_name = 'Partner'
    verbose_name_plural = 'Partners'
    managed = True
    ordering = ('id',)

  def __str__(self):
    return self.name

  def thumb(self):
    if self.image:
      return mark_safe('<img src="%s" style="width:50px;height:50px;" alt="" />' % self.image.url)
    else:
      return "No Image"
    thumb.short_description = 'Partner Image'
    thumb.allow_tags = True

  def img(self):
    if self.image:
      return mark_safe('<img src="%s" style="height:150px;" alt="" />' % self.image.url)
    else:
      return "No Image"
    img.short_description = 'Partner Image'
    img.allow_tags = True

class Project(models.Model):
  image = models.ImageField(upload_to='projects/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg", "jpeg"])])
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  partners = MultiSelectField(choices=PARTNER_CHOICES, null=False, blank=False)
  title = models.CharField(max_length=75, null=False, blank=False)
  description = models.TextField(null=True, blank=True)
  article = HTMLField(null=True, blank=True)
  ongoing = models.BooleanField(default=False)
  slug = models.SlugField(max_length=255, unique=True, db_index=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    verbose_name = 'Project'
    verbose_name_plural = 'Projects'
    managed = True
    ordering = ('author__username', '-updated_at')
    

  def __str__(self):
    return "%s - %s" % (self.author, self.title) if self.author else self.title

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = create_slug(self.title)
    if not self.updated_at:
      self.updated_at = timezone.now()
    super(Project, self).save(*args, **kwargs)
  
  def thumb(self):
    if self.image:
      return mark_safe('<img src="%s" style="width:50px;height:50px;" alt="%s" />' % (self.image.url, self.title))
    else:
      return "No Image"
    thumb.short_description = 'Project Image'
    thumb.allow_tags = True

  def img(self):
    if self.image:
      return mark_safe('<img src="%s" style="height:150px;" alt="%s" />' % (self.image.url, self.title))
    else:
      return "No Image"
    img.short_description = 'Project Image'
    img.allow_tags = True

class Resource(models.Model):
  image = models.ImageField(upload_to='resources/',validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg", "jpeg"])])
  title = models.CharField(max_length=150, null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  link = models.URLField(null=True, blank=True)

  class Meta:
    verbose_name = 'Resource'
    verbose_name_plural = 'Resources'
    managed = True
    ordering = ('id',)

  def __str__(self):
    return self.title

  def thumb(self):
    if self.image:
      return mark_safe('<img src="%s" style="width:50px;height:50px;" alt="%s" />' % (self.image.url, self.title))
    else:
      return "No Image"
    thumb.short_description = 'Resource Image'
    thumb.allow_tags = True

  def img(self):
    if self.image:
      return mark_safe('<img src="%s" style="height:150px;" alt="%s" />' % (self.image.url, self.title))
    else:
      return "No Image"
    img.short_description = 'Resource Image'
    img.allow_tags = True

class Contact(models.Model):
  image = models.ImageField(upload_to='contact/',validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg", "jpeg"])])
  title = models.CharField(max_length=75, null=True, blank=True)
  phone = models.CharField(max_length=25, null=True, blank=True)
  address = models.CharField(max_length=150, null=True, blank=True)
  email = models.EmailField(null=True, blank=True)
  linktree = models.URLField(null=True, blank=True)

  class Meta:
    verbose_name = 'Contact'
    verbose_name_plural = 'Contacts'
    managed = True
    ordering = ('id',)

  def __str__(self):
    return self.title

  def thumb(self):
    if self.image:
      return mark_safe('<img src="%s" style="width:50px;height:50px;" alt="%s" />' % (self.image.url, self.title))
    else:
      return "No Image"
    thumb.short_description = 'Contact Logo 1000x1000'
    thumb.allow_tags = True

  def img(self):
    if self.image:
      return mark_safe('<img src="%s" style="height:150px;" alt="%s" />' % (self.image.url, self.title))
    else:
      return "No Image"
    img.short_description = 'Contact Logo 1000x1000'
    img.allow_tags = True
  