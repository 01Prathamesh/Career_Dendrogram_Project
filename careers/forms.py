# # careers/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import UserProfile
# from .models import CareerPath, Role


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['current_role', 'career_goals', 'photo', 'date_of_birth', 'location', 'education']
    
#     date_of_birth = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date'}),
#         input_formats=['%Y-%m-%d']  # Optional, adjust if needed
#     )


# class CareerPathForm(forms.ModelForm):
#     class Meta:
#         model = CareerPath
#         fields = ['title', 'description']
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 4}),
#         }

# class RoleForm(forms.ModelForm):
#     class Meta:
#         model = Role
#         fields = ['title', 'career_path', 'prerequisites']
#         widgets = {
#             'prerequisites': forms.CheckboxSelectMultiple(),
#         }


# class TestForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         questions = kwargs.pop('questions', [])
#         super().__init__(*args, **kwargs)

#         for question1 in questions:
#             self.fields[f'question_{question1.id}'] = forms.ChoiceField(
#                 choices=[(option1, option1) for option1 in question1.options1],
#                 label=question1.question_text,
#                 widget=forms.RadioSelect
#             )

# Updated Code
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import UserProfile, CareerPath, Role, TestQuestion

# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['current_role', 'career_goals', 'photo', 'date_of_birth', 'location', 'education']
    
#     date_of_birth = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date'}),
#         input_formats=['%Y-%m-%d']  # Optional, adjust if needed
#     )

# class CareerPathForm(forms.ModelForm):
#     class Meta:
#         model = CareerPath
#         fields = ['title', 'description']
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 4}),
#         }

# class RoleForm(forms.ModelForm):
#     class Meta:
#         model = Role
#         fields = ['title', 'career_path', 'prerequisites']
#         widgets = {
#             'prerequisites': forms.CheckboxSelectMultiple(),
#         }

# class TestForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         questions = kwargs.pop('questions', [])
#         super().__init__(*args, **kwargs)
        
#         for question in questions:
#             # Extract choices from the JSON field
#             choices = [(choice, choice) for choice in question.choices]
            
#             self.fields[f'question_{question.id}'] = forms.ChoiceField(
#                 choices=choices,
#                 label=question.text,
#                 widget=forms.RadioSelect
#             )


