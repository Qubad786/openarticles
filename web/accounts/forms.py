from django import forms

from web.accounts.models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'gender', 'role']

        layout = [
            ("Text", "<h4 class=\"ui dividing header\">Register</h4>"),
            ("Field", "username"),
            ("Field", "password"),
            ('Two Fields',
             ("Field", "first_name"),
             ("Field", "last_name"),
             ),
        ]


class SignInForm(forms.Form):

    class Meta:
        layout = [
            ("Text", "<h4 class=\"ui dividing header\">Sign in</h4>"),
            ("Field", "username"),
            ("Field", "password"),
        ]

    username = forms.CharField(label='Enter username', required=True)
    password = forms.CharField(widget=forms.PasswordInput())
