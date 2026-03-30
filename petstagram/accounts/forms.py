from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ["email"]



class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = "__all__"


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]

        labels = {
            'first_name': "First Name:",
            'last_name': "Last Name:",
            'date_of_birth': "Date of Birth:",
            'profile_picture': "Profile Picture:",
        }