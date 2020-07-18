# auth:zbk
# create date:7.10
# description:

from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    UserID = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "UserID", 'autofocus': ''}))
    Password = forms.CharField(label="密码",max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    captcha = CaptchaField(label='验证码',error_messages={"invalid": "验证码错误","required":"验证码不能为空"})

class RegisterForm(forms.Form):

    UserID = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    UserName = forms.CharField(label="用户昵称", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    Password2 = forms.CharField(label="确认密码", max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    Email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码',error_messages={"invalid": "验证码错误","required":"验证码不能为空"})

class EvaluationForm(forms.Form):
    pass