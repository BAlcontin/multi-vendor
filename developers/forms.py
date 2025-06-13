from django import forms
from .models import Developer


class DeveloperForm(forms.ModelForm):

    # developer_banner = forms.FileField(widget=forms.FileInput(
    #     attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])

    class Meta:
        model = Developer
        fields = ['developer_name', 'developer_banner']


# class OpeningHourForm(forms.ModelForm):
#     class Meta:
#         model = OpeningHour
#         fields = ['day', 'from_hour', 'to_hour', 'is_closed']
