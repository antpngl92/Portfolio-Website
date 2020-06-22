from django import forms
from .models import *

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['project_name' , 'project_description', 'project_link', 'project_image']
