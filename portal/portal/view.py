from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from PortalModel.models import Data, UserExtension
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
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
    form = DataForm()
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse('upload ok!')
        else:
            return HttpResponse('not valid')
    else:
        return render(request, 'formtest.html', {'form':form})
        