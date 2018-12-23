from django import forms


class UserForm(forms.Form):
    inputTel = forms.CharField(label='inputTel', max_length=12)
    inputPassword = forms.CharField(label='inputPassword', widget=forms.PasswordInput())


class ResetForm(forms.Form):
    oldpaw1 = forms.CharField(label='oldpaw1', widget=forms.PasswordInput())
    newpaw1 = forms.CharField(label='newpaw1', widget=forms.PasswordInput())
