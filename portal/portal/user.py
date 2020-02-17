from PortalModel.models import Data, UserExtension
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.db import IntegrityError


def register_(request):
    login_dict = {
        'emailNotExistedAlert': "",
        'passwordIncorrect': "",
        'useremail': ""
    }
    request.encoding = 'utf-8'
    if request.method == 'POST':        
        user_name = request.POST.get('n')
        user_email = request.POST.get('e')
        pwd = request.POST.get('p')
        pwd_ = request.POST.get('p_')
        register_dict = {
            'userNameAlert': "",
            'emailAlert': "",
            'passwordAlert': "",
            'passwordCheckAlert': ""
        }
        # length judge
        legal = True
        if user_name is None or len(user_name) == 0 or len(user_name) > 50:
            register_dict['userNameAlert'] = "用户名长度不符合要求"
            legal = False
        if user_email is None or len(user_email) == 0 or len(user_email) > 150:
            register_dict['emailAlert'] = "邮箱长度不符合要求"
            legal = False
        if pwd is None or len(pwd) == 0 or len(pwd) > 30:
            register_dict['passwordAlert'] = "密码长度不符合要求"
            legal = False
        if not (pwd.strip() == pwd_.strip()):
            register_dict['passwordCheckAlert'] = "与初始密码不同"
            legal = False

        if legal == False:
            return render(request, "register.html", login_dict)
        
        try:
            user = UserExtension.objects.create_user(
                username=user_email, email=user_email, password=pwd)
        except IntegrityError:
            register_dict['emailAlert'] = "邮箱地址已被注册"
            return render(request, 'register.html', register_dict)
        user.nickname = user_name
        user.save()
        login_dict['useremail'] = user_email
    return render(request, 'login.html', login_dict)   


def login_(request):
    login_dict = {
        'emailNotExistedAlert': "",
        'passwordIncorrect': "",
        'useremail': ""
    }
    request.encoding = 'utf-8'
    if request.method == 'POST':
        user_email = request.POST.get('e')
        pwd = request.POST.get('p')
        # length judge
        legal = True
        if user_email is None or len(user_email) == 0 or len(user_email) > 150:
            login_dict['emailNotExistedAlert'] = "邮箱长度不符合要求"
            legal = False
        if pwd is None or len(pwd) == 0 or len(pwd) > 30:
            login_dict['passwordIncorrect'] = "密码长度不符合要求"
            legal = False
        if legal == False:
            return render(request, "login.html", login_dict)
        try:
            UserExtension.objects.get(email=user_email)
        except UserExtension.DoesNotExist:
            login_dict['emailNotExistedAlert'] = "该用户不存在"
            return render(request, "login.html", login_dict)
        user = authenticate(username=user_email, password=pwd)
        if user is None:
            login_dict['passwordIncorrect'] = "密码错误"
            login_dict['useremail'] = user_email
            return render(request, "login.html", login_dict)
        else:
            login(request, user)
            return HttpResponseRedirect("/")
    return render(request, "login.html", login_dict)


def logout_(request):
    logout(request)
    return HttpResponseRedirect("/")


def user_page(request):
    return render(request, "user_page.html")