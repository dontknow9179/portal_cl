from django import forms

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