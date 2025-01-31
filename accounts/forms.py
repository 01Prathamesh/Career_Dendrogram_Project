
# Updated Code
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile, CareerPath, Role
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already taken.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username is already taken.")
        return username

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    # Separate first_name and last_name fields (avoiding the 'name' field redundancy)
    first_name = forms.CharField(max_length=30, required=False, label='First Name')
    last_name = forms.CharField(max_length=30, required=False, label='Last Name')

    location = forms.CharField(max_length=150, required=False, label='Location')
    education_qualification = forms.CharField(max_length=150, required=False, label='Education Qualification')
    
    # Date of birth input
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = UserProfile
        fields = ['photo', 'first_name', 'last_name', 'date_of_birth', 'location', 'education_qualification', 'current_role', 'career_goals']

    def save(self, commit=True):
        # Save the user profile and update the user's first_name and last_name from the form fields
        user_profile = super().save(commit=False)
        
        # Set the user fields (first_name, last_name) from the form data
        if self.cleaned_data.get('first_name'):
            self.instance.user.first_name = self.cleaned_data['first_name']
        if self.cleaned_data.get('last_name'):
            self.instance.user.last_name = self.cleaned_data['last_name']
        
        # Save the user object
        if commit:
            self.instance.user.save()  # Save the user model first
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
        # Extract the 'questions' argument passed into the form
        questions = kwargs.pop('questions', [])
        super().__init__(*args, **kwargs)

        for question in questions:
            # Extract choices from the 'choices' attribute (assuming it's a list or tuple)
            choices = [(choice, choice) for choice in question.choices]

            # Dynamically create a ChoiceField for each question
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=choices,
                label=question.text,
                widget=forms.RadioSelect,
                # The Below are some options to display the questions options.
                # widget=forms.CheckboxSelectMultiple,
                # widget=forms.Select,
                # widget=forms.SelectMultiple,
                # widget=forms.TextInput,
                # widget=forms.FileInput,
                required=False,  # Allow the user to leave it empty for custom validation
            )

    def clean(self):
        """
        Perform form-level validation (if needed).
        This method ensures that users are selecting options for each question.
        """
        cleaned_data = super().clean()

        # Loop through all the fields to check for unselected questions
        for field in self.fields:
            # Check if the user has selected an option for the field
            if cleaned_data.get(field) == '--Select--' or not cleaned_data.get(field):
                # Add an error for the field if no option was selected
                self.add_error(field, '*Please select an option.*')

        return cleaned_data

from django.contrib.auth.forms import PasswordChangeForm
    
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))