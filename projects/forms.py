from django.forms import ModelForm, widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    
    class Meta:
        model = Project
        # fields = "__all__"
        exclude = ['vote_total', 'vote_ratio']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class':'input input--text','placeholder':'Enter Title'})
        self.fields['description'].widget.attrs.update({'class':'input input--textarea--sm','placeholder':'Enter Description'})
        self.fields['demo_link'].widget.attrs.update({'class':'input input--text','placeholder':'Enter Live Demo Link'})
        self.fields['source_link'].widget.attrs.update({'class':'input input--text','placeholder':'Enter Code Link'})