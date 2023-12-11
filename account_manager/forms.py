from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, BlogPost


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = (
            'user_type', 'first_name', 'last_name', 'profile_picture', 'username', 'email', 'password1', 'password2',
            'address_line1', 'city', 'state', 'pincode')


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'draft']
        widgets = {'category': forms.Select(attrs={'readonly': 'readonly'})}
