from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from entries.models import Entry
from djangostatistics.models import Interaction


def index(request, entry_slug):
    entry = get_object_or_404(Entry, slug=entry_slug)
    Interaction.objects.create(interaction_type=f'Read Entry {entry.title}')
    return TemplateResponse(request, "entries/index.html", {
        "entry": entry
    })
