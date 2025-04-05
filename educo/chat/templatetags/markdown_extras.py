# myapp/templatetags/markdown_extras.py
from django import template
import markdown

register = template.Library()

@register.filter(name='markdown')
def markdown_filter(value):
    """Converts Markdown text to HTML."""
    return markdown.markdown(value)
