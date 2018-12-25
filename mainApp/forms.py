from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from master_office.models import OrderLine, Order, Service
from django.forms import inlineformset_factory
from django.contrib.auth.models import Group


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Имя', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class OrderLineForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all(), required=True, label="Услуга")
    brand_name = forms.CharField(label="Брэнд", max_length=20)
    device_name = forms.CharField(label="Модель", max_length=20)
    serial_id = forms.CharField(label="Серийный номер", max_length=20)
    trouble_description = forms.CharField(widget=forms.Textarea, label="Описание проблемы", max_length=100)

    class Meta:
        model = OrderLine
        fields = ['service', 'brand_name', 'device_name', 'serial_id', 'trouble_description']

    def save(self, commit=False):
        line = super(forms.ModelForm, self).save(commit=False)
       # line.service = self.serice
        if commit:
            line.save()
        return line
