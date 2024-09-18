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
subjects = (
    ('--Select--','--Select--'),
    ('Science','Science'),
    ('Mathematics','Mathematics'),
    ('Literature','Literature'),
    ('Arts','Arts'),
    ('History','History'),
    ('Technology','Technology'),
    ('Busniness','Busniness'),
)
hobbies = (
    ('--Select--','--Select--'),
    ('painting', 'Painting'),
    ('writing', 'Writing'),
    ('playing_sports', 'Playing sports'),
    ('gaming', 'Gaming'),
    ('cooking', 'Cooking'),
    ('volunteering', 'Volunteering'),
    ('crafting', 'Crafting'),
)

work_preference = (
    ('--Select--','--Select--'),
    ('team', 'In a team'),
    ('independently', 'Independently'),
    ('mix', 'A mix of both'),
)

environment = (
    ('--Select--','--Select--'),
    ('office', 'Office'),
    ('outdoors', 'Outdoors'),
    ('remote', 'Remote'),
    ('laboratory', 'Laboratory'),
    ('classroom', 'Classroom'),
)

skills = (
    ('--Select--','--Select--'),
    ('communication', 'Communication'),
    ('analytical_thinking', 'Analytical thinking'),
    ('creativity', 'Creativity'),
    ('leadership', 'Leadership'),
    ('technical_skills', 'Technical skills'),
)

technology_comfort = (
    ('--Select--','--Select--'),
    ('very_comfortable', 'Very comfortable'),
    ('somewhat_comfortable', 'Somewhat comfortable'),
    ('not_comfortable', 'Not comfortable'),
)

creativity_importance = (
    ('--Select--','--Select--'),
    ('very_important', 'Very important'),
    ('somewhat_important', 'Somewhat important'),
    ('not_important', 'Not important'),
)

career_importance = (
    ('--Select--','--Select--'),
    ('job_security', 'Job security'),
    ('high_salary', 'High salary'),
    ('creativity', 'Creativity'),
    ('helping_others', 'Helping others'),
    ('work_life_balance', 'Work-life balance'),
)

age_group = (
    ('--Select--','--Select--'),
    ('children', 'Children'),
    ('teenagers', 'Teenagers'),
    ('adults', 'Adults'),
    ('all_ages', 'All ages'),
)

healthcare_interest = (
    ('--Select--','--Select--'),
    ('yes', 'Yes'),
    ('no', 'No'),
    ('somewhat', 'Somewhat'),
)

public_speaking = (
    ('--Select--','--Select--'),
    ('enjoy_it', 'I enjoy it'),
    ('can_manage', 'I can manage'),
    ('prefer_to_avoid', 'I prefer to avoid it'),
)

business_interest = (
    ('--Select--','--Select--'),
    ('management', 'Management'),
    ('finance', 'Finance'),
    ('marketing', 'Marketing'),
    ('entrepreneurship', 'Entrepreneurship'),
    ('human_resources', 'Human Resources'),
)

environmental_interest = (
    ('--Select--','--Select--'),
    ('yes', 'Yes'),
    ('no', 'No'),
    ('somewhat', 'Somewhat'),
)

it_interest = (
    ('--Select--','--Select--'),
    ('cybersecurity', 'Cybersecurity'),
    ('software_development', 'Software Development'),
    ('networking', 'Networking'),
    ('database_management', 'Database Management'),
    ('web_development', 'Web Development'),
)

financial_decisions = (
    ('--Select--','--Select--'),
    ('analytical_calculated', 'Analytical and calculated'),
    ('gut_feeling', 'Gut feeling'),
    ('mix', 'A mix of both'),
)

hands_on_work = (
    ('--Select--','--Select--'),
    ('yes', 'Yes'),
    ('no', 'No'),
    ('sometimes', 'Sometimes'),
)

arts_interest = (
    ('--Select--','--Select--'),
    ('visual_arts', 'Visual arts'),
    ('music', 'Music'),
    ('literature', 'Literature'),
    ('theater', 'Theater'),
    ('dance', 'Dance'),
)

research_interest = (
    ('--Select--','--Select--'),
    ('love_it', 'I love it'),
    ('can_manage', 'I can manage'),
    ('prefer_practical', 'I prefer practical work'),
)

entrepreneurship_interest = (
    ('--Select--','--Select--'),
    ('yes', 'Yes'),
    ('no', 'No'),
    ('maybe', 'Maybe'),
)

learning_style = (
    ('--Select--','--Select--'),
    ('hands_on', 'Hands-on'),
    ('visual', 'Visual'),
    ('auditory', 'Auditory'),
    ('reading_writing', 'Reading/Writing'),
)

class Test(forms.Form):
    Which_subjects_did_you_enjoy_most_in_school = forms.ChoiceField(choices=subjects)
    What_hobbies_do_you_spend_the_most_time_on = forms.ChoiceField(choices=hobbies)
    How_do_you_prefer_to_work = forms.ChoiceField(choices=work_preference)
    What_type_of_environment_do_you_thrive_in = forms.ChoiceField(choices=environment)
    Which_of_the_following_skills_do_you_consider_your_strongest = forms.ChoiceField(choices=skills)
    How_comfortable_are_you_with_technology = forms.ChoiceField(choices=technology_comfort)
    How_important_is_creativity_in_your_career_choice = forms.ChoiceField(choices=creativity_importance)
    What_is_most_important_to_you_in_a_career = forms.ChoiceField(choices=career_importance)
    Which_age_group_do_you_prefer_to_work_with = forms.ChoiceField(choices=age_group)
    Are_you_interested_in_healthcare_or_helping_others = forms.ChoiceField(choices=healthcare_interest)
    How_do_you_feel_about_public_speaking = forms.ChoiceField(choices=public_speaking)
    What_aspect_of_business_interests_you_the_most = forms.ChoiceField(choices=business_interest)
    Are_you_passionate_about_environmental_issues = forms.ChoiceField(choices=environmental_interest)
    Which_area_of_IT_interests_you_the_most = forms.ChoiceField(choices=it_interest)
    How_do_you_approach_financial_decisions = forms.ChoiceField(choices=financial_decisions)
    Do_you_enjoy_hands_on_work = forms.ChoiceField(choices=hands_on_work)
    Which_area_of_arts_and_culture_fascinates_you = forms.ChoiceField(choices=arts_interest)
    How_do_you_feel_about_research_and_analysis = forms.ChoiceField(choices=research_interest)
    Are_you_interested_in_entrepreneurship = forms.ChoiceField(choices=entrepreneurship_interest)
    Which_of_the_following_best_describes_your_learning_style = forms.ChoiceField(choices=learning_style) 
