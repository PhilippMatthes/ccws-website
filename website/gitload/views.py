import json

from django.shortcuts import get_object_or_404
from djangostatistics.models import Interaction
from django.http import Http404, JsonResponse
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt

from gitload.models import GitloadToken


@csrf_exempt
def trigger_gitload(request):
    Interaction.objects.create(interaction_type='Trigger gitload')
    if request.method != 'POST':
        print("post")
        raise Http404
    token_value = request.POST.get('token_value')
    if not token_value:
        payload = json.loads(request.body)
        token_value = payload.get('token_value')
        if not token_value:
            raise Http404
    get_object_or_404(GitloadToken, pk=token_value)
    call_command('gitload')
    response = JsonResponse({'success': True})
    response["Access-Control-Allow-Origin"] = "*"
    return response
