from .models import StudentSearch
from django import forms


class StudentGeneralSearch(forms.ModelForm):
    class Meta:
        model = StudentSearch
        fields = ['query']
        labels = {'query':'Search'}
        widgets = {
            'query': forms.TextInput(attrs = {'class':'form-control', 'autofocus':True})
            }


