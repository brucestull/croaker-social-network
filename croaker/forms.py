from django import forms

from croaker.models import Croak


class CroakForm(forms.ModelForm):
    """
    Form for the `Croak` model.
    """
    tiny_body = forms.CharField(
        required=True,
        widget = forms.widgets.Textarea(
            attrs={
                # 'rows': 6,
                # 'cols': 25,
                "placeholder": "What's the world need to hear?",
                "class": "text-area is-success is-medium",
            },
        ),
        # label="Tiny Body",
        label="",
    )

    class Meta:
        model = Croak
        exclude = [
            'user'
        ]
