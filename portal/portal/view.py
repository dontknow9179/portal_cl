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
        'userNameAlert': "",
        'emailAlert': "",
        'passwordAlert': "",
        'passwordCheckAlert': ""
    }
    return render(request, 'register.html', register_dict)


def showdata(request):
    showdata_dict = {}
    # showdata_dict['success_add'] = False
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            datafile = form.cleaned_data['datafile']
            description = form.cleaned_data['description']
            data = Data(nickname=request.user.userextension.nickname, 
                        email=request.user.email, datafile=datafile, 
                        description=description)
            data.save() 
            showdata_dict['success_add'] = True         
            form = DataForm()
        else:
            pass
    else:
        form = DataForm()

    if request.user.is_authenticated:    
        data = Data.objects.filter(email=request.user.email)
        showdata_dict['data'] = data
    else:
        pass
    
    showdata_dict['form'] = form
    return render(request, 'showdata.html', showdata_dict)


def deletedata(request):
    if request.method == 'POST' and request.user.is_authenticated:
        delete_list = request.POST.getlist('checkbox_list')
        print(delete_list)
        showdata_dict = {}
        showdata_dict['success_del'] = True
        for data_id in delete_list:
            try:
                Data.objects.filter(id=data_id).delete()
            except Data.DoesNotExist:
                print('delete: data does not exist')
                showdata_dict['success_del'] = False

        data = Data.objects.filter(email=request.user.email)
        showdata_dict['data'] = data
        showdata_dict['form'] = DataForm()
        return render(request, 'showdata.html', showdata_dict)
    else:
        pass

        