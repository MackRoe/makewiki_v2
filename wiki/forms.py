from django import forms
from wiki.models import Page
from django.forms import ModelForm


class PageForm(ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Page
        fields = ['title', 'content', 'author']
