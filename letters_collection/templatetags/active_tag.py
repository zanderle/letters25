from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def add_active(request, names, includes='', by_path=False):
    """ Return the string 'active' current request.path is same as name

    Keyword aruguments:
    request  -- Django request object
    name     -- name of the url or the actual path (separated with semicolon)
    by_path  -- True if name contains a url instead of url name
    """
    names = names.split(';')
    for name in names:
        if not name:
            continue
        if by_path:
            path = name
        else:
            path = reverse(name)

        if request.path == path:
            return ' active '
    includes = includes.split(';')
    for include in includes:
        if include and include in request.path:
            return ' active '

    return ''
