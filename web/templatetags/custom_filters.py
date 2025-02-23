from django import template

register = template.Library()


@register.filter(name="partners_list")
def partners_list(partners):
    plist = []

    for i in partners:
        i = i.replace("Loesje ", "")
        plist.append(i.lower())
    return (" ").join(plist)


@register.filter(name="status_filter")
def status_filter(status):
    if status:
        return "ongoing"
    return "past"
