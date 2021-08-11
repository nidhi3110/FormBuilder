from django import forms
from django.db.models import fields
from .models import Survey,SurveyData

class createSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ["title", "description"] 

class surveyForm(forms.ModelForm):
    class Meta:
        model = SurveyData
        fields = [
                    "first_name",
                    "last_name" ,
                    "email",
                    "contact",
                    "field1" ,
                    "field2",
                    "field3",
                    "image"
                ]

