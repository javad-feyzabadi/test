from django import template

from .. models import Category


register = template.Library()

@register.simple_tag
def title():
    return "https://telegram.me/javad_feyzabadi"


@register.inclusion_tag('blog/partials/category_navbar.html')
def category_navbar():
    return {
        'cat' : Category.objects.filter(status=True)
    }

