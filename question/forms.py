from django import forms
from question import models

class UserForm(forms.ModelForm):
    account = forms.CharField(label='账号', required=True)
    passwd = forms.CharField(label="密码", required=True, widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('account', 'passwd')