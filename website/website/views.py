from django.template.response import TemplateResponse

from entries.models import Entry


"""
Serve a homepage view with the most relevant entries.

Entries can be filtered by a search query.
"""
def index(request):
    entries = Entry.objects.all()
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
