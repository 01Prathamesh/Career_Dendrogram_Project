# # accounts/forms.py

# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
# from .models import UserProfile

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name')

# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name')



# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['photo', 'date_of_birth', 'location', 'education']
    
#     # Add a field for the username if you want to allow users to change it
#     username = forms.CharField(max_length=150, required=False, label='Username')
    
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
#         if user:
#             self.fields['username'].initial = user.username


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

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


from django.core.validators import MaxValueValidator, MinValueValidator
YES_OR_NO = (
    ('yes','yes'),
    ('no','no'),
)
certifications = (
    ('shell programming','shell programming'),
    ('machine learning','machine learning'),
    ('app development','app development'),
    ('python','python'),
    ('r programming','r programming'),
    ('information security','information security'),
    ('hadoop','hadoop'),
    ('distro making','distro making'),
    ('full stack','full stack'),
)
skills = (
    ('poor','poor'),
    ('medium','medium'),
    ('excellent','excellent'),
)
subject = (
    ('cloud computing','cloud computing'),
    ('networks','networks'),
    ('hacking','hacking'),
    ('Computer Architecture','Computer Architecture'),
    ('parallel computing','parallel computing'),
    ('IOT','IOT'),
    ('data engineering','data engineering'),
    ('Software Engineering','Software Engineering'),
    ('Management','Management'),
)
career = (
    ('system developer','system developer'),
    ('Business process analyst','Business process analyst'),
    ('developer','developer'),
    ('testing','testing'),
    ('security','security'),
    ('cloud computing','cloud computing'),
)
studies = (
    ('higherstudies','higherstudies'),
    ('job','job')
)
companies =(
    ('Web Services','Web Services'),
    ('SAaS services','SAaS services'),
    ('Sales and Marketing','Sales and Marketing'),
    ('Testing and Maintainance Services','Testing and Maintainance Services'),
    ('product development','product development'),
    ('BPA','BPA'),
    ('Service Based','Service Based'),
    ('Product based','Product based'),
    ('Cloud Services','Cloud Services'),
    ('Finance','Finance'),
)
books = (
    ('Prayer books','Prayer books'),
    ('Childrens','Childrens'),
    ('Travel','Travel'),
    ('Romance','Romance'),
    ('Cookbooks','Cookbooks'),
    ('Self help','Self help'),
    ('Drama','Drama'),
    ('Math','Math'),
    ('Religion-Spiritality','Religion-Spiritality'),
    ('Anthology','Anthology'),
    ('Trilogy','Trilogy'),
    ('Autobiographies','Autobiographies'),
    ('Mystery','Mystery'),
    ('Diaries','Diaries'),
    ('Journals','Journals'),
    ('History','History'),
    ('Art','Art'),
    ('Dictionaries','Dictionaries'),
    ('Horror','Horror'),
    ('Encyclopedias','Encyclopedias'),
    ('Action and Adventure','Action and Adventure'),
    ('Fantasy','Fantasy'),
    ('Comics','Comics'),
    ('Science fiction','Science fiction'),
    ('Series','Series'),
    ('Guide','Guide'),
    ('Biographies','Biographies'),
    ('Health','Health'),
    ('Satire','Satire'),
    ('Science','Science'),
    ('Poetry','Poetry'),
    
)
behaviour = (
    ('stubborn','stubborn'),
    ('gentle','gentle'),
)
management_technical = (
    ('Technical','Technical'),
    ('Management','Management'),
)
worker = (
    ('smart worker','smart worker'),
    ('hard worker','hard worker'),
)

class Test(forms.Form):
    academic_percentage_in_operating_system = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_algorithm = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_programming_concepts = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_software_engineering = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_computer_networks = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_electronics_subjects = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_computer_architecture = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_mathematics = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    percentage_in_communication_skills = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    how_many_hours_in_a_day_you_can_work = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(24)])
    Rate_your_logical_quotient=forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    How_may_hackathon_have_you_participated=forms.IntegerField()
    Rate_your_coding_skills=forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    Rate_your_public_speaking=forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    can_work_long_time_before_system = forms.ChoiceField(choices = YES_OR_NO)
    self_learning_capability = forms.ChoiceField(choices=YES_OR_NO)
    which_certifications_do_you_prefer = forms.ChoiceField(choices=certifications)
    any_talenttests_taken= forms.ChoiceField(choices=YES_OR_NO)
    scale_your_reading_and_writing_skills = forms.ChoiceField(choices=skills)
    scale_your_memory_capability_score = forms.ChoiceField(choices=skills)
    Interested_subjects = forms.ChoiceField(choices=subject)
    interested_career_area = forms.ChoiceField(choices=career)
    what_do_you_prefer_job_or_higher_studies = forms.ChoiceField(choices=studies)
    type_of_company_you_prefer = forms.ChoiceField(choices=companies)
    intereaction_with_seniors = forms.ChoiceField(choices=YES_OR_NO)
    do_you_love_games = forms.ChoiceField(choices=YES_OR_NO)
    type_of_books_you_prefer = forms.ChoiceField(choices=books)
    most_likely_behaviour = forms.ChoiceField(choices=behaviour)
    what_you_prefer_managemet_or_technical = forms.ChoiceField(choices= management_technical)
    have_you_ever_worked_with_teams = forms.ChoiceField(choices=YES_OR_NO)
    Are_you_an_Introvert= forms.ChoiceField(choices=YES_OR_NO) 
