from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from entries.models import Entry


def index(request, entry_slug):
    entry = get_object_or_404(Entry, slug=entry_slug)
    return TemplateResponse(request, "entries/index.html", {
        "entry": entry
    })
