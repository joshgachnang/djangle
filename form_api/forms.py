from django import forms


class BaseAPIForm(forms.BaseForm):
    pass


class FormAPI(object):
    def __init__(self):
        self.serializers = []

    def register(self, serializer):
        self.serializers.append(serializer)
        print 'forms', self.serializers, dir(serializer)


api = FormAPI()