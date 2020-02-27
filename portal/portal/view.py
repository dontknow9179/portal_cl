from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from PortalModel.models import Data, Task, UserExtension, submission_delete
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from django import forms
from PortalModel.forms import DataForm, TaskForm
import os
from . import settings


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
    if request.method == 'POST' and request.user.is_authenticated:
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            datafile = form.cleaned_data['datafile']
            description = form.cleaned_data['description']
            data = Data(nickname=request.user.userextension.nickname, 
                        email=request.user.email, datafile=datafile, 
                        description=description)
            data.save()         
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
        showdata_dict = {}
        if delete_list is None or len(delete_list) == 0:
            showdata_dict['error_message'] = '删除文件失败：未选择要删除的文件'
        else:
            for data_id in delete_list:
                try:
                    data = Data.objects.get(id=data_id)
                    submission_delete(Data,data)
                    data.delete()
                except Data.DoesNotExist:
                    print('delete: data does not exist')
                    showdata_dict['error_message'] = '删除文件失败：不存在要删除的文件'            

        data = Data.objects.filter(email=request.user.email)
        showdata_dict['data'] = data
        showdata_dict['form'] = DataForm()
        return render(request, 'showdata.html', showdata_dict)
    else:
        pass


def renamedata(request):
    if request.method == 'POST' and request.user.is_authenticated:    
        new_name = request.POST.get('new_name')
        data_id = request.POST.get('data_id')
        showdata_dict = {}
        if new_name is None or len(new_name) == 0 or len(new_name) > 70 or data_id is None:
            showdata_dict['error_message'] = '重命名文件出错'
        else:
            try:
                data = Data.objects.get(id=data_id)
                p_dir = 'user_'+request.user.email
                new_path = os.path.join(settings.MEDIA_ROOT, os.path.join(p_dir, new_name))
                os.rename(data.datafile.path, new_path)
                data.datafile.name = os.path.join(p_dir, new_name)
                data.save()
                # print(data.datafile.path)
                # print(data.datafile.name)
            except Data.DoesNotExist:
                print('rename: data does not exist')
                showdata_dict['error_message'] = '重命名文件失败：不存在要重命名的文件'
            except FileExistsError:
                print('rename: name duplication')
                showdata_dict['error_message'] = '重命名文件失败：存在同名的文件'
            except:
                print('Unexpected error:', sys.exc_info()[0])
                showdata_dict['error_message'] = '重命名文件失败'

        data = Data.objects.filter(email=request.user.email)       
        showdata_dict['data'] = data
        showdata_dict['form'] = DataForm()
        return render(request, 'showdata.html', showdata_dict)
    else:
        pass   


def showtask(request):
    showtask_dict = {}
    if request.method == 'POST' and request.user.is_authenticated:
        form = TaskForm(request.POST, user_email=request.user.email)        
        if form.is_valid():           
            taskname = form.cleaned_data['taskname']
            description = form.cleaned_data['description']
            data_list = form.cleaned_data['content']
            content = ' '.join(data_list) 
            task = Task(taskname=taskname, description=description, content=content, email=request.user.email)
            task.save()
            form = TaskForm(user_email=request.user.email)
        else:
            pass
    elif request.user.is_authenticated:   
        form = TaskForm(user_email=request.user.email)     

    else:
        form = TaskForm()

    if request.user.is_authenticated:
        tasks = Task.objects.filter(email=request.user.email)
        showtask_dict['tasks'] = tasks
    else:
        pass

    showtask_dict['form'] = form
    return render(request, 'showtask.html',showtask_dict)


def deletetask(request):
    if request.method == 'POST' and request.user.is_authenticated:
        delete_list = request.POST.getlist('checkbox_list')        
        showtask_dict = {}
        if delete_list is None or len(delete_list) == 0:
            showtask_dict['error_message'] = '删除任务失败：未选择要删除的任务'
        else:
            for task_id in delete_list:
                try:
                    task = Task.objects.get(id=task_id)
                    task.delete()
                except Task.DoesNotExist:
                    print('delete: task does not exist')
                    showtask_dict['error_message'] = '删除任务失败：不存在要删除的任务'            

        tasks = Task.objects.filter(email=request.user.email)
        showtask_dict['tasks'] = tasks
        showtask_dict['form'] = TaskForm(user_email=request.user.email)
        return render(request, 'showtask.html', showtask_dict)
    else:
        pass


def renametask(request):
    if request.method == 'POST' and request.user.is_authenticated:    
        new_name = request.POST.get('new_name')
        task_id = request.POST.get('task_id')
        showtask_dict = {}
        if new_name is None or len(new_name) == 0 or len(new_name) > 70 or task_id is None:
            showtask_dict['error_message'] = '重命名任务出错'
        else:
            try:
                task = Task.objects.get(id=task_id)
                task.taskname = new_name
                task.save()
            except Task.DoesNotExist:
                print('rename: task does not exist')
                showdata_dict['error_message'] = '重命名任务失败：不存在要重命名的任务'
        tasks = Task.objects.filter(email=request.user.email)
        showtask_dict['tasks'] = tasks
        showtask_dict['form'] = TaskForm(user_email=request.user.email)
        return render(request, 'showtask.html', showtask_dict)
    else:
        pass
    

def test(request):
    return render(request, 'test.html')