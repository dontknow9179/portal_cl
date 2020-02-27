from django import forms
from django.contrib.auth.models import User
from PortalModel.models import Data, UserExtension

class DataForm(forms.Form):
    datafile = forms.FileField(
        label='',
        required=True,
        error_messages={'required':'文件不能为空'}
    )
    description = forms.CharField(
        max_length=200,
        required=False,
        label='备注(选填)',
        widget=forms.Textarea(),
        error_messages={'max_length':'备注不能超过200字'}
    )
    

class TaskForm(forms.Form):
    taskname = forms.CharField(
        max_length=70,
        required=True,
        label='任务名',
        error_messages={'required':'任务名不能为空','max_length':'任务名不能超过70个字'}
    )
    description = forms.CharField(
        max_length=200,
        required=False,
        label='备注(选填)',
        widget=forms.Textarea(),
        error_messages={'max_length':'备注不能超过200字'}
    )
    content = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='选择任务所需的数据'
    )
    def __init__(self, *args, **kwargs):
        user_email = kwargs.pop('user_email', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['content'].choices = [(x.id, x.filename) for x in Data.objects.filter(email=user_email)]


class LoginForm(forms.Form):
    user_email = forms.EmailField(
        max_length=150,
        label='输入邮箱',
        error_messages={'required':'邮箱不能为空'},
        widget=forms.EmailInput(attrs={'placeholder':'输入邮箱'})
    )
    pwd = forms.CharField(
        max_length=128,
        label='输入密码',
        widget=forms.PasswordInput(attrs={'placeholder':'输入密码'}),
        error_messages={'required':'密码不能为空'}
    )

class RegisterForm(forms.Form):
    user_name = forms.CharField(
        max_length=50, 
        label='输入用户名',
        error_messages={'required':'用户名不能为空'}
    )
    user_email = forms.EmailField(
        max_length=150,
        label='输入邮箱',
        error_messages={'required':'邮箱不能为空'}
    )
    pwd1 = forms.CharField(
        max_length=128,
        label='输入密码',
        widget=forms.PasswordInput(),
        error_messages={'required':'密码不能为空'}
    )
    pwd2 = forms.CharField(
        max_length=128,
        label='确认密码',
        widget=forms.PasswordInput(),
        error_messages={'required':'密码不能为空'}
    )
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('pwd1')
        confirm_password = cleaned_data.get('pwd2')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(u'两次密码输入不一致，请重新输入')