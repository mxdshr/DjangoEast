from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label='fa fa-user',
                               widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'请输入用户名'}))
    password = forms.CharField(label='fa fa-lock',
                               widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'请输入密码'}))

    # 验证用户名密码是否正确
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码错误')
        else:
            self.cleaned_data['user'] = user

        return self.cleaned_data


# 注册表单
class RegForm(forms.Form):
    username = forms.CharField(label='fa fa-user',max_length=30,min_length=3,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入3-30位的用户名'}))
    email = forms.EmailField(label='fa fa-envelope',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'}))
    password = forms.CharField(label='fa fa-lock',min_length=6,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入不少于6位的密码'}))
    password_again = forms.CharField(label='fa fa-lock',min_length=6,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入再次密码'}))

    # 验证部分
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已存在')
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('密码输入不一致')
        return password

