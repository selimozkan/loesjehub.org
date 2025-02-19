from .models import GeneralSetting

def PageSetting(request):
  return {
    'pagesetting': GeneralSetting.objects.first(),
  }