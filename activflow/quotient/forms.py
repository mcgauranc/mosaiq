"""Custom Forms"""

from django import forms
from django.db.models import (
    CharField)


class CustomForm(forms.ModelForm):
    """Sample Custom form"""
    sample_id = CharField("Sample Id:", max_length=200, editable=False)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()
