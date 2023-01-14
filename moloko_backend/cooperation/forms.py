from django import forms

from moloko_backend.cooperation.models import TermOfCooperation


class TermsListForm(forms.Form):
    type = forms.ChoiceField(choices=TermOfCooperation.Type.choices)
