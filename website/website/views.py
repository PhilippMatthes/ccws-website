from django.template.response import TemplateResponse

from entries.models import Entry


def index(request):
    return TemplateResponse(request, "index.html", {
        "entries": Entry.objects.all(),
    })
