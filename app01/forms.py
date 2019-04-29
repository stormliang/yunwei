#!/Users/liangyufeng/venv/bin/python3
# _*_ coding:utf-8 _*_
from django import forms
from app01 import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义操作
        for field in self.fields.values():
            # field.widget.attrs['class'] = 'form-control'
            field.widget.attrs.update({'class': 'form-control'})  # 迭代添加


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义操作
        for field in self.fields.values():
            # field.widget.attrs['class'] = 'form-control'
            field.widget.attrs.update({'class': 'form-control'})  # 迭代添加
