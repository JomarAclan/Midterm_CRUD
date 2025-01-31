from django import forms
from .models import BMIRecord

class BMIRecordForm(forms.ModelForm):
    class Meta:
        model = BMIRecord
        fields = ['weight', 'height', 'age', 'gender']