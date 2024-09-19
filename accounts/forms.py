
# Updated Code
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile, CareerPath, Role

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'photo', 'date_of_birth', 'location', 'education_qualification', 'current_role', 'career_goals' ]

    # Add a field for the username if you want to allow users to change it
    # username = forms.CharField(max_length=150, required=False, label='Username')
    name = forms.CharField(max_length=150, required=False, label='Full Name')
    location= forms.CharField(max_length=150, required=False, label='Location')
    education_qualification= forms.CharField(max_length=150, required=False, label='Education Qualification')
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']  # Optional, adjust if needed
    )
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username

    def save(self, commit=True):
        user_profile = super().save(commit=False)
        if self.cleaned_data.get('username'):
            user = self.instance.user
            user.username = self.cleaned_data['username']
            user.save()
        if commit:
            user_profile.save()
        return user_profile

class CareerPathForm(forms.ModelForm):
    class Meta:
        model = CareerPath
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['title', 'career_path', 'prerequisites']
        widgets = {
            'prerequisites': forms.CheckboxSelectMultiple(),
        }

class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', [])
        super().__init__(*args, **kwargs)
        
        for question in questions:
            # Extract choices from the JSON field
            choices = [(choice, choice) for choice in question.choices]
            
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=choices,
                label=question.text,
                widget=forms.RadioSelect
            )

