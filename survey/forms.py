from django import forms
from .models import GeneralInformation, BusinessType, BusinessField, BusinessSize, StrategyOperation, GeneralFeedback

class GeneralInformationForm(forms.ModelForm):
    class Meta:
        model = GeneralInformation
        fields = "__all__"

class BusinessTypeForm(forms.ModelForm):
    class Meta:
        model = BusinessType
        fields = "__all__"

class BusinessFieldForm(forms.ModelForm):
    class Meta:
        model = BusinessField
        fields = "__all__"

class BusinessSizeForm(forms.ModelForm):
    class Meta:
        model = BusinessSize
        fields = "__all__"

class StrategyOperationForm(forms.ModelForm):
    class Meta:
        model = StrategyOperation
        fields = "__all__"
        widgets = {
            field: forms.RadioSelect(choices=StrategyOperation.LIKERT_CHOICES)
            for field in StrategyOperation._meta.get_fields()
            if field.name != "submitted_at"
        }

class GeneralFeedbackForm(forms.ModelForm):
    class Meta:
        model = GeneralFeedback
        fields = "__all__"
