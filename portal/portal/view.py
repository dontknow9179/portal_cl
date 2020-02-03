from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from PortalModel.models import Data, UserExtension
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from django import forms
from PortalModel.forms import DataForm


def homepage(request):
    return render(request, 'index.html')


def login_page(request):
    login_dict = {
        'emailNotExistedAlert': "",
        'passwordIncorrect': "",
        'useremail': ""
    }
    return render(request, 'login.html', login_dict)


def register_page(request):
    register_dict = {
        'emailExistedAlert': ""
    }
    return render(request, 'register.html', register_dict)


def testform(request):   
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            datafile = form.cleaned_data['datafile']
            description = form.cleaned_data['description']
            data = Data(nickname=request.user.userextension.nickname, 
                        email=request.user.email, datafile=datafile, 
                        description=description)
            data.save()
            # return render(request, 'formtest.html', {'form':form})
            return HttpResponse('upload ok!')
        else:
            return render(request, 'formtest.html', {'form':form})
    else:
        form = DataForm()
        return render(request, 'formtest.html', {'form':form})
        