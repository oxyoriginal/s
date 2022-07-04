from django import forms
from django.forms import ModelForm

from s_app import models
from s_app.models import Service

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'title', 'price', 'text']

class SearchForm(forms.Form):
    searchtext = forms.CharField(label='Search', initial='type here')
    where = forms.ChoiceField(label='Where', choices=((0, '----'), (1, 'Title'), (2, 'Text')))
    price_edit = forms.IntegerField(label='Price', initial=0)
    count = forms.ChoiceField(label='count', choices=((0, '----'), (1, 'More than'), (2, 'Less than')))


