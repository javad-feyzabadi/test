from django import template
from django.db.models import Count,Q
from .. models import Article,Category
from datetime import datetime, timedelta



register = template.Library()

@register.simple_tag
def title():
    return "https://telegram.me/javad_feyzabadi"


@register.inclusion_tag('blog/partials/category_navbar.html')
def category_navbar():
    return {
        'cat' : Category.objects.filter(status=True)
    }


@register.inclusion_tag('blog/partials/sidebar.html')
def popular_articles():
    last_month = datetime.today() - timedelta(days=30)
    return {
        'articles' : Article.objects.filter(status="P").annotate(
            count=Count('hits',filter=Q(articlehit__created__gt = last_month))
        ).order_by('-count','-publish')[:5],
        'title':'Article Most Viewer'
    }


@register.inclusion_tag('blog/partials/sidebar.html')
def hot_articles():
    last_month = datetime.today() - timedelta(days=30)
    return {
        'articles' : Article.objects.filter(status="P").annotate(
            count=Count('comments',filter=Q(comments__posted__gt = last_month) and Q(comments__content_type_id = 6))
        ).order_by('-count','-publish')[:5],
        'title':'Article Hot Month'
    }

