from typing import Optional
import json

from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.forms import model_to_dict
from django.http import Http404, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from entries.models import Entry
from djangostatistics.models import Interaction


def get_optional_int(key_name: str, data: dict) -> Optional[int]:
    """
    Get and validate an integer parameter from a data dictionary.
    """
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


def get_optional_bool(key_name: str, data: dict) -> Optional[bool]:
    """
    Get and validate a boolean parameter from a data dictionary.
    """
    parameter = data.get(key_name)
    if parameter is None:
        return None
    if isinstance(parameter, bool):
        return parameter
    if isinstance(parameter, int):
        return bool(parameter)
    if isinstance(parameter, str):
        if parameter.lower() == "true":
            return True
        if parameter.lower() == "false":
            return False
    raise ValidationError(
        f'Boolean parameter "{key_name}" was supplied '
        f'with the value {parameter!r} but is not a boolean value.'
    )


@csrf_exempt
def get_entries(request):
    Interaction.objects.create(interaction_type='GET Entries Lazy API Access')
    if request.method != 'GET':
        raise Http404()
    try:
        limit = get_optional_int('limit', request.GET) or 5
    except ValidationError:
        raise Http404()

    entries = Entry.objects \
        .order_by('-updated')[:limit]

    response = JsonResponse({
        'limit': limit,
        'entries': json.loads(serializers.serialize('json', entries))
    })

    response["Access-Control-Allow-Origin"] = "*"

    return response

