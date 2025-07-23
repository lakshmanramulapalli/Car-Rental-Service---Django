from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    city = forms.CharField(max_length=100, required=False)
    pincode = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'first_name', 'last_name', 'phone', 'address', 'city', 'pincode']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'phone', 'address', 'city', 'pincode']