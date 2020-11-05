import json

from typing import Optional

from django.core.exceptions import ValidationError
from django.http import Http404, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from entries.models import Entry


"""
Get and validate an integer parameter from a data dictionary.
"""
def get_optional_int(key_name: str, data: dict) -> Optional[int]:
    parameter = data.get(key_name)
    if parameter is None:
        return None
    if isinstance(parameter, int):
        return parameter
    if isinstance(parameter, str):
        try:
            return int(parameter)
        except ValueError:
            pass
    raise ValidationError(
        f'Integer parameter "{key_name}" was supplied '
        f'with the value {parameter!r} but is not an integer value.'
    )


"""
Get a list of blog entries via a json endpoint.
"""
@csrf_exempt
def get_entries(request):
    if request.method != 'GET':
        raise Http404()
    try:
        limit = get_optional_int('limit', request.GET) or 5
    except ValidationError:
        raise Http404()

    entries = Entry.objects \
        .order_by('created')[:limit]

    response = JsonResponse({
        'limit': limit,
        'entries': json.loads(serializers.serialize('json', entries))
    })

    response["Access-Control-Allow-Origin"] = "*"
    return response

