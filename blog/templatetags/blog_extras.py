from django import template
from django.utils.html import strip_tags
import re
from html import unescape

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Template filter to get an item from a dictionary using a variable as the key.
    Usage: {{ dictionary|get_item:key }}
    """
    return dictionary.get(key)

@register.filter(name='truncate_title')
def truncate_title(value, length):
    """
    Truncates a string to a specified length, adding an ellipsis if it exceeds the length.
    Usage: {{ title|truncate_title:50 }}
    """
    length = int(length)
    if len(value) > length:
        return value[:length] + "..."
    return value

@register.filter(name='clean_html')
def clean_html(value, length=100):
    """
    Removes HTML tags and entities from content and truncates to the specified length.
    Usage: {{ content|clean_html:100 }}
    """
    if not value:
        return ""

    # Strip HTML tags
    text = strip_tags(value)

    # Decode HTML entities (like &nbsp; and &hellip;)
    text = unescape(text)

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # Truncate to specified length
    length = int(length)
    if len(text) > length:
        return text[:length] + "..."
    return text
