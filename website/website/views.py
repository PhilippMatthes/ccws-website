from django.template.response import TemplateResponse

from entries.models import Entry


def index(request):
    """
    Serve a homepage view with the most relevant entries.

    Entries can be filtered by a search query.
    """
    entries = Entry.objects.order_by('-created')
    if request.method == 'GET':
        query = request.GET.get('query')
        if isinstance(query, str) and query:
            entries = entries.filter(
                title__icontains=query
            ) | entries.filter(
                description__icontains=query
            ) | entries.filter(
                markdown__icontains=query
            )
    return TemplateResponse(request, 'index.html', {
        'entries': entries,
    })
