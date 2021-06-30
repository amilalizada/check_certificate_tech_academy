from django import forms
from django.utils.translation import gettext as _
from main.models import Certificate


class HomeForm(forms.Form):
    verification = forms.CharField(label='verification' , widget=forms.TextInput(attrs={
        'class':'form-control',
    }),max_length=40)

    # recaptcha_input = forms.CharField(label='verification' , widget=forms.TextInput(attrs={
    #     'class':'form-control',

    # }),max_length=40)

    def clean_verification(self):
        cleaned_data = self.cleaned_data
        certificate_number = cleaned_data.get('verification')
        if not Certificate.objects.filter(certificade_number=certificate_number).exists():
            raise forms.ValidationError(_('Bele bir sertifikat tapilmadi'))
        return certificate_number


