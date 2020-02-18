from django import forms
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': _('E-mail address')}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Password')}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is None:
            raise forms.ValidationError(_('Incorrect email/password.'))
        login(self.request, user)
