from .models import SecurityRiskAspects
from django import forms

class SecurityRiskAspects_Form(forms.ModelForm):
    class Meta:
        model = SecurityRiskAspects
        fields = (
            'RiskAspect_Name',
            'RiskAspect_Description'
        )

class SecurityRiskAspects_Edit(forms.ModelForm):
    class Meta:
        model = SecurityRiskAspects
        fields = (
            'RiskAspect_Name',
            'RiskAspect_Description'
        )