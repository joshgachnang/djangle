from django.http import JsonResponse

from django_angular_forms import form_api


additional_field_attrs = {
    'string': ['max_length', 'min_length'],
    'datetime': [],
    'date': []
}


def render_serializers(request, name=None):
    api = form_api.api
    response = {}
    for name, serializer in api.serializers.items():
        instance = serializer()
        response[name] = {
            'title': name,
            'fields': _get_fields(instance),
        }
    print response
    return JsonResponse(response)


def _get_fields(instance):
    fields = {}
    for field_name, field in instance.fields.items():
        print field, field.type_label, dir(field)
        fields[field_name] = {}
        for attr in ['help_text', 'required', 'label',
                     'read_only', 'default', 'type_name']:
            fields[field_name][attr] = getattr(field, attr)
        # Add field specific additional fields
        for attr in additional_field_attrs[field.type_label]:
            fields[field_name][attr] = getattr(field, attr)
    return fields
