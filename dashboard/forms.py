from django import forms
from .models import SecurityFinding


class SecurityFindingForm(forms.ModelForm):

    class Meta:
        model = SecurityFinding
        fields = [
            'title',
            'description',
            'category',
            'severity',
            'status',
            'assigned_to',
        ]

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }