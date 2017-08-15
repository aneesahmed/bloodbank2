# coding=utf-8
from django import forms
from patient.models import Bloodgroup


class BloodgroupForm(forms.ModelForm):
   class Meta:
        model =  Bloodgroup
        fields = "__all__"
        #labels =
        widgets = {'bloodgroup': forms.Textarea(attrs={'cols': 80})}