from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))
    
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegisrtationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Фамилия'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Никнейм'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'E-mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')