from django import forms
from proposal.models import Proposal
import re
from django.core.exceptions import ValidationError


class ProposalForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if re.match(r"\d", name):
            raise ValidationError("Имя не должно начинаться с цифры")
        return name

    class Meta:
        model = Proposal
        fields = ["name", "phone", "mail", "message", "files"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "tel",
                    "id": "exampleFormControlPhone",
                    "name": "phone",
                    "placeholder": "+7(987)654-32-10",
                }
            ),
            "mail": forms.EmailInput(
                attrs={
                    "type": "email",
                    "class": "form-control",
                    "id": "exampleFormControlEmail",
                    "name": "email",
                    "placeholder": "name@example.com",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "id": "exampleFormControlTextarea",
                    "name": "message",
                    "minlength": "20",
                }
            ),
        }
