from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
