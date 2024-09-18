# # accounts/views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from .forms import CustomUserCreationForm
# from .forms import UserProfileForm
# from .models import UserProfile

# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

# @login_required
# def profile_view(request):
#     user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=user_profile, user=request.user)
#         if form.is_valid():
#             # Update the user profile and save
#             form.save()
#             # Optionally update the username
#             if form.cleaned_data['username']:
#                 request.user.username = form.cleaned_data['username']
#                 request.user.save()
#             return redirect('profile')
#     else:
#         form = UserProfileForm(instance=user_profile, user=request.user)
    
#     return render(request, 'accounts/profile.html', {'form': form})



# Updated Code
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, UserProfileForm, CareerPathForm, RoleForm, TestForm, RegistrationForm, Test
from .models import UserProfile, TestQuestion, UserTestResponse
from .models import CareerPath
from .models import Role
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

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
    x={}
    if request.method == 'POST':
            form = Test(request.POST)
            x['1) Which subjects did you enjoy most in school?'] = request.POST.get('Which_subjects_did_you_enjoy_most_in_school')
            x['2) What hobbies do you spend the most time on?'] = request.POST.get('What_hobbies_do_you_spend_the_most_time_on')
            x['3) How do you prefer to work?'] = request.POST.get('How_do_you_prefer_to_work')
            x['4) What type of environment do you thrive in?'] = request.POST.get('What_type_of_environment_do_you_thrive_in')
            x['5) Which of the following skills do you consider your strongest?'] = request.POST.get('Which_of_the_following_skills_do_you_consider_your_strongest')
            x['6) How comfortable are you with technology?'] = request.POST.get('How_comfortable_are_you_with_technology')
            x['7) How important is creativity in your career choice?'] = request.POST.get('How_important_is_creativity_in_your_career_choice')
            x['8) What is most important to you in a career?'] = request.POST.get('What_is_most_important_to_you_in_a_career')
            x['9) Which age group do you prefer to work with?'] = request.POST.get('Which_age_group_do_you_prefer_to_work_with')
            x['10) Are you interested in healthcare or helping others?'] = request.POST.get('Are_you_interested_in_healthcare_or_helping_others')
            x['11) How do you feel about public speaking?'] = request.POST.get('How_do_you_feel_about_public_speaking')
            x['12) What aspect of business interests you the most?'] = request.POST.get('What_aspect_of_business_interests_you_the_most')
            x['13) Are you passionate about environmental issues?'] = request.POST.get('Are_you_passionate_about_environmental_issues')
            x['14) Which area of IT interests you the most?'] = request.POST.get('Which_area_of_IT_interests_you_the_most')
            x['15) How do you approach financial decisions?'] = request.POST.get('How_do_you_approach_financial_decisions')
            x['16) Do you enjoy hands-on work?'] = request.POST.get('Do_you_enjoy_hands_on_work')
            x['17) Which area of arts and culture fascinates you?'] = request.POST.get('Which_area_of_arts_and_culture_fascinates_you')
            x['18) How do you feel about research and analysis?'] = request.POST.get('How_do_you_feel_about_research_and_analysis')
            x['19) Are you interested in entrepreneurship?'] = request.POST.get('Are_you_interested_in_entrepreneurship')
            x['20) Which of the following best describes your learning style?'] = request.POST.get('Which_of_the_following_best_describes_your_learning_style')
		
            print(x)
            career = fun(x)
            context= {'career':career}
            return render(request,'test_results.html',context)
    context = {'form':form}
    return render(request,'start_test.html',context)

def fun(dict1):
	return "Complete Function fun(dict1) in views.py in app folder to predict the proper career from roo_data.csv in line 82 "

def test_results(request):
    # Implement logic to handle and display test results
    return render(request, 'test_results.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

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
    
    return render(request, 'accounts/profile.html', {'form': form})

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
