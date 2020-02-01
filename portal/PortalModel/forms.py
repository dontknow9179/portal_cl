from django import forms

class DataForm(forms.Form):
    datafile = forms.FileField(
        label='选择上传的文件',
    )
    description = forms.CharField(
        max_length=200,
        required=False,
        label='备注',
        help_text='选填'
    )