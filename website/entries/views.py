import re
from urllib.parse import unquote
from os.path import join

from django.conf import settings
from django.template.response import TemplateResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.views.static import serve

from entries.models import Entry



def index(request, slug):
    """Return a view for a specific blog entry."""
    entry = get_object_or_404(Entry, slug=slug)
    return TemplateResponse(request, "entries/index.html", {
        "entry": entry
    })


def serve_attachment(request, slug, path):
    """Serve an attachment for a blog entry."""
    if re.search('^(images|attachments)/', path) is None:
        raise PermissionDenied

    if '..' in unquote(path):
        raise PermissionDenied

    filesystem_path = join(slug, path)
    return serve(request, filesystem_path, settings.REPOSITORY_ROOT)
