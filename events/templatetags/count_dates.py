from django import template
from django.template import Node
from events.models import Event
register = template.Library()


def build_category_list(parser, token):
    """
    {% get_category_list %}
    """
    return CategoryObject()

class CategoryObject(Node):
    def render(self, context):
        context['events'] = Event.objects.all()
        return ''

register.tag('get_category_list', build_category_list)
