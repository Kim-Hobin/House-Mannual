from django import forms
from . import models


class CreateItemView(forms.ModelForm):
    class Meta:

        model = models.Accommodation
        fields = (
            "name",
            "avatar",
            "description",
            "background_image",
            "address",
            "phone_number",
            "check_in",
            "check_out",
            "wifi",
            "facility",
            "recycle",
            "house_rule",
            "content",
            "slug",
            "host",
        )
        widgets = {
            "host": forms.HiddenInput(),
        }

    def save(self, *args, **kwargs):
        accommodations = super().save(commit=True)
        return accommodations
