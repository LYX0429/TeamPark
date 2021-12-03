from django import forms
from pages import models


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ('project_name', 'project_desc')
        error_messages = {
        }


class ServerForm(forms.ModelForm):
    class Meta:
        model = models.Server
        fields = ('project', 'product')
        error_messages = {
        }