from django.shortcuts import render

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


#
# def createAccount(request):
#     if request.method == 'POST':
#         name = request.GET['name']
#         email = request.GET['email']
#         password = request.GET['password']
#         name.save()
#         email.save()
#         password.save()
#         return render(request, '/')