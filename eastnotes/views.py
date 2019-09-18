from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth.models import User
from eastnotes.form import LoginForm, RegForm


# 显示登录页面、进行登录操作
def login(request):
    # 此处只有登录的操作，验证的部分在forms.py完成
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from',reverse('blog:index')))  # 重定向到上一个页面
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request, 'login/login.html', context)


# 显示注册页面、进行注册操作
def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password']
            email = reg_form.cleaned_data['email']

            # 注册用户
            user = User()
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()

            # 注册后自动登录
            user = auth.authenticate(username=username,password=password)
            auth.login(request, user)

            # 跳转到进入注册页面之前的页面
            return redirect(request.GET.get('from',reverse('blog:index')))  # 重定向到上一个页面

    else:
        reg_form = RegForm()
    context = {}
    context['reg_form'] = reg_form
    return render(request, 'login/register.html', context)
