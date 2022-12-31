from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

