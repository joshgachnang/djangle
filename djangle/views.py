from django.http import JsonResponse

from djangle import form_api


additional_field_attrs = {
    'string': ['max_length', 'min_length'],
    'datetime': [],
    'date': [],
    'url': [],
    'choice': ['choices']
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
    fields = []
    for field_name, field in instance.fields.items():
        f = {}
        for attr in ['help_text', 'required', 'label',
                     'read_only', 'default', 'type_name']:
            f[attr] = getattr(field, attr)
        # Add field specific additional fields
        for attr in additional_field_attrs.get(field.type_label, []):
            f[attr] = getattr(field, attr)
            if attr == 'choices':
                print 'choices', getattr(field, attr)
        fields.append(f)
    return fields
