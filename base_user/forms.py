from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext as _

User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password '}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'country',
            'username',
            'email',
            'phone_number',
            'privacy_policy',
        )
    
        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Last Name'}),
            'username':forms.TextInput(attrs={'placeholder':'Username'}),
            'email':forms.TextInput(attrs={'placeholder':'E-Mail Address'}),
            'phone_number':forms.TextInput(attrs={'placeholder':'Phone Number'}),
        }
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages["Password isn't match"],
                code="password_isn't match",
            )
        return password2

    

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form--control',
        'placeholder': 'myemail@domain.com',
        'type': 'email',
        'name': 'email'
        }))



class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password', 'class': 'form--control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password', 'class': 'form--control'}),
    )

