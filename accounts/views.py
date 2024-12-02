# Updated Code
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, UserProfileForm, CareerPathForm, RoleForm, RegistrationForm
from .questions import Test
from .models import UserProfile
from .models import CareerPath
from .models import Role
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseBadRequest

def home(request):
    return render(request, 'accounts/home.html')

def career_list(request):
    careers = CareerPath.objects.all()
    return render(request, 'careers/career_list.html', {'careers': careers})

def dendrogram(request):
    return render(request, 'careers/dendrogram.html')

def role_list(request):
    roles = Role.objects.all()
    return render(request, 'careers/role_list.html', {'roles': roles})

def add_career_path(request):
    if request.method == 'POST':
        form = CareerPathForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('career_list')
    else:
        form = CareerPathForm()
    return render(request, 'careers/add_career_path.html', {'form': form})

def edit_career_path(request, pk):
    career_path = get_object_or_404(CareerPath, pk=pk)
    if request.method == 'POST':
        form = CareerPathForm(request.POST, instance=career_path)
        if form.is_valid():
            form.save()
            return redirect('career_list')
    else:
        form = CareerPathForm(instance=career_path)
    return render(request, 'careers/edit_career_path.html', {'form': form})

def delete_career_path(request, pk):
    career_path = get_object_or_404(CareerPath, pk=pk)
    if request.method == 'POST':
        career_path.delete()
        return redirect('career_list')
    return render(request, 'careers/delete_career_path.html', {'career_path': career_path})

def career_paths_data(request):
    career_paths = CareerPath.objects.all()
    data = {
        'name': 'Career Paths',
        'children': [
            {
                'name': career.title,
                'children': [
                    {'name': role.title} for role in Role.objects.filter(career_path=career)
                ]
            }
            for career in career_paths
        ]
    }
    return JsonResponse(data)


def add_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm()
    return render(request, 'careers/add_role.html', {'form': form})

def edit_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'careers/edit_role.html', {'form': form})

def delete_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('role_list')
    return render(request, 'careers/delete_role.html', {'role': role})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'careers/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def start_test(request):
    form = Test()
    if request.method == 'POST':
        form = Test(request.POST)
        if form.is_valid():
            # Collecting the user's answers from the form
            user_answer = {
                'How_do_you_prefer_to_work': form.cleaned_data['How_do_you_prefer_to_work'],
                'Which_subjects_did_you_enjoy_most_in_school': form.cleaned_data['Which_subjects_did_you_enjoy_most_in_school'],
                'What_hobbies_do_you_spend_the_most_time_on': form.cleaned_data['What_hobbies_do_you_spend_the_most_time_on'],
                'What_type_of_environment_do_you_thrive_in': form.cleaned_data['What_type_of_environment_do_you_thrive_in'],
                'Which_of_the_following_skills_do_you_consider_your_strongest': form.cleaned_data['Which_of_the_following_skills_do_you_consider_your_strongest'],
                'How_comfortable_are_you_with_technology': form.cleaned_data['How_comfortable_are_you_with_technology'],
                'How_important_is_creativity_in_your_career_choice': form.cleaned_data['How_important_is_creativity_in_your_career_choice'],
                'What_is_most_important_to_you_in_a_career': form.cleaned_data['What_is_most_important_to_you_in_a_career'],
                'Which_age_group_do_you_prefer_to_work_with': form.cleaned_data['Which_age_group_do_you_prefer_to_work_with'],
                'Are_you_interested_in_healthcare_or_helping_others': form.cleaned_data['Are_you_interested_in_healthcare_or_helping_others'],
                'How_do_you_feel_about_public_speaking': form.cleaned_data['How_do_you_feel_about_public_speaking'],
                'What_aspect_of_business_interests_you_the_most': form.cleaned_data['What_aspect_of_business_interests_you_the_most'],
                'Are_you_passionate_about_environmental_issues': form.cleaned_data['Are_you_passionate_about_environmental_issues'],
                'Which_area_of_IT_interests_you_the_most': form.cleaned_data['Which_area_of_IT_interests_you_the_most'],
                'How_do_you_approach_financial_decisions': form.cleaned_data['How_do_you_approach_financial_decisions'],
                'Do_you_enjoy_hands_on_work': form.cleaned_data['Do_you_enjoy_hands_on_work'],
                'Which_area_of_arts_and_culture_fascinates_you': form.cleaned_data['Which_area_of_arts_and_culture_fascinates_you'],
                'How_do_you_feel_about_research_and_analysis': form.cleaned_data['How_do_you_feel_about_research_and_analysis'],
                'Are_you_interested_in_entrepreneurship': form.cleaned_data['Are_you_interested_in_entrepreneurship'],
                'Which_of_the_following_best_describes_your_learning_style': form.cleaned_data['Which_of_the_following_best_describes_your_learning_style'],
            }

            request.session['user_answers'] = user_answer
            print("Session User Answers Set:", request.session.get('user_answers'))
            return redirect('test_results')
        else:
            print("Form errors:", form.errors)  # Print errors if the form is invalid
            messages.error(request, "Please correct the errors below.")
    
    return render(request, 'start_test.html', {'form': form})


def test_results(request):
    user_answers = request.session.get('user_answers')
    if user_answers is None:
        return redirect('start_test')
    
    print("User Answers from Session:", user_answers)

    suggested_career_paths = determine_career_paths(user_answers)

    return render(request, 'test_results.html', {
        'user_answers': user_answers,
        'suggested_career_paths': suggested_career_paths,
    })

def determine_career_paths(user_answers):
    print("User Answers:", user_answers)
    suggested_paths = []

    # Define career paths based on user inputs
    paths_mapping = {
        'How_do_you_prefer_to_work': {
            'In a team': 'Project Manager',
            'Independently': 'Freelancer',
            'A mix of both': 'Team Leader',
        },
        'Which_subjects_did_you_enjoy_most_in_school': {
            'Science': 'Engineer',
            'Mathematics': 'Data Analyst',
            'Literature': 'Author',
            'Arts': 'Graphic Designer',
            'History': 'Historian',
            'Technology': 'Software Developer',
        },
        'What_hobbies_do_you_spend_the_most_time_on': {
            'Painting': 'Art Teacher',
            'Writing': 'Content Creator',
            'Playing sports': 'Sports Coach',
            'Gaming': 'Game Developer',
            'Cooking': 'Chef',
            'Volunteering': 'Nonprofit Worker',
            'Crafting': 'Craft Business Owner',
        },
        'What_type_of_environment_do_you_thrive_in': {
            'Office': 'Corporate Employee',
            'Outdoors': 'Environmental Scientist',
            'Remote': 'Remote Worker',
            'Laboratory': 'Lab Technician',
            'Classroom': 'Teacher',
        },
        'Which_of_the_following_skills_do_you_consider_your_strongest': {
            'Communication': 'Public Relations Specialist',
            'Analytical Thinking': 'Data Scientist',
            'Creativity': 'Creative Director',
            'Leadership': 'Team Leader',
            'Technical Skills': 'IT Specialist',
        },
        'How_comfortable_are_you_with_technology': {
            'Very Comfortable': 'Software Developer',
            'Somewhat Comfortable': 'IT Support',
            'Not Comfortable': 'Customer Service Representative',
        },
        'How_important_is_creativity_in_your_career_choice': {
            'Very Important': 'Creative Director',
            'Somewhat Important': 'Marketing Specialist',
            'Not Important': 'Operations Manager',
        },
        'What_is_most_important_to_you_in_a_career': {
            'Job Security': 'Government Employee',
            'High Salary': 'Investment Banker',
            'Creativity': 'Graphic Designer',
            'Helping Others': 'Healthcare Professional',
            'Work-life balance': 'Remote Worker',
        },
        'Are_you_interested_in_healthcare_or_helping_others': {
            'Yes': 'Healthcare Professional',
            'No': None,
            'Somewhat': 'Social Worker',
        },
        'How_do_you_feel_about_public_speaking': {
            'I enjoy it': 'Public Speaker',
            'Can Manage': 'Trainer',
            'Prefer To Avoid': 'Researcher',
        },
        'What_aspect_of_business_interests_you_the_most': {
            'Management': 'Manager',
            'Finance': 'Financial Analyst',
            'Marketing': 'Marketing Specialist',
            'Entrepreneurship': 'Startup Founder',
            'Human Resources': 'HR Specialist',
        },
        'Are_you_passionate_about_environmental_issues': {
            'Yes': 'Conservationist',
            'No': None,
            'Somewhat': 'Sustainability Consultant',
        },
        'Which_area_of_IT_interests_you_the_most': {
            'CyberSecurity': 'Cybersecurity Analyst',
            'Software Development': 'Software Engineer',
            'Networking': 'Network Engineer',
            'Database Management': 'Database Administrator',
            'Web Development': 'Web Developer',
        },
        'How_do_you_approach_financial_decisions': {
            'Analytical and calculated': 'Financial Analyst',
            'Gut feeling': 'Entrepreneur',
            'A mix of both': 'Business Consultant',
        },
        'Do_you_enjoy_hands_on_work': {
            'Yes': 'Mechanic',
            'No': 'Office Worker',
            'Sometimes': 'Technician',
        },
        'Which_area_of_arts_and_culture_fascinates_you': {
            'Visual Arts': 'Artist',
            'Music': 'Musician',
            'Literature': 'Writer',
            'Theater': 'Actor',
            'Dance': 'Choreographer',
        },
        'How_do_you_feel_about_research_and_analysis': {
            'I love it': 'Research Scientist',
            'Can Manage': 'Market Research Analyst',
            'Prefer Practical': 'Hands-On Technician',
        },
        'Are_you_interested_in_entrepreneurship': {
            'Yes': 'Startup Founder',
            'No': None,
            'Maybe': 'Business Consultant',
        },
        'Which_of_the_following_best_describes_your_learning_style': {
            'Hands-On': 'Workshop Instructor',
            'Visual': 'Graphic Designer',
            'Auditory': 'Public Speaker',
            'Reading/Writing': 'Author',
        },
        'Which_age_group_do_you_prefer_to_work_with': {
            'Children': 'Child Psychologist',
            'Teenagers': 'Youth Counselor',
            'Adults': 'Career Coach',
            'All Ages': 'Community Organizer',
        },
    }

    for key, mapping in paths_mapping.items():
        suggested_paths.append(mapping.get(user_answers.get(key)))

    suggested_paths = list(filter(None, suggested_paths))
    print("Final Suggested Paths:", suggested_paths)
    return list(set(suggested_paths))  # Return unique paths


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None  # Or handle appropriately
    return render(request, 'accounts/profile.html', {'profile': user_profile})


@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            # No need to manually update the username if using UserProfileForm
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'accounts/profile.html', {'form': form, 'profile': user_profile, 'user': request.user})

@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/edit_profile.html', {'form': form})


def career_paths_api(request):
    data = list(CareerPath.objects.values('id', 'name', 'parent_id'))
    return JsonResponse(data, safe=False)

def plagiarism(request):
    return render(request, 'accounts/plagiarism.html')


def science_view(request):
    return render(request, 'careers/options/science.html')

def commerce_view(request):
    return render(request, 'careers/options/commerce.html')