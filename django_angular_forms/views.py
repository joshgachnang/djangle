from django.http import JsonResponse

from django_angular_forms import form_api


def render_serializers(request, name=None):
    api = form_api.api
    response = {}
    for name, serializer in api.serializers.items():
        instance = serializer()
        response[name] = {
            'fields': _get_fields(instance),
        }
    print response
    return JsonResponse(response)


def _get_fields(instance):
    fields = {}
    for field_name, field in instance.fields.items():
        fields[field_name] = {}
        for attr in ['help_text', 'required', 'label',
                     'read_only', 'default', ]:
            fields[field_name][attr] = getattr(field, attr)
    return fields
