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
    # question= TestQuestion.objects.all()
    # if request.method == 'POST':
    #     form = TestForm(request.POST, questions=TestQuestion.objects.all())
    #     if form.is_valid():
    #         for question in TestQuestion.objects.all():
    #             selected_option = form.cleaned_data.get(f'question_{question.id}')
    #             if selected_option:
    #                 UserTestResponse.objects.create(
    #                     user=request.user,
    #                     question=question,
    #                     selected_option=selected_option
    #                 )
    #         return redirect('test_results')
    # else:
    #     questions = TestQuestion.objects.all()
    #     form = TestForm(questions=questions)
    # return render(request, 'start_test.html', {'form': form})
    form = Test()
    x={}
    if request.method == 'POST':
            form = Test(request.POST)
            x['academic_percentage_in_operating_system']= request.POST.get('academic_percentage_in_operating_system')
            x['percentage_in_algorithm']=request.POST.get('percentage_in_algorithm')		
            x['percentage_in_programming_concepts']=request.POST.get('percentage_in_programming_concepts')		
            x['percentage_in_software_engineering']=request.POST.get('percentage_in_software_engineering')		
            x['percentage_in_computer_networks']=request.POST.get('percentage_in_computer_networks')		
            x['percentage_in_electronics_subjects']=request.POST.get('percentage_in_electronics_subjects')		
            x['percentage_in_computer_architecture']=request.POST.get('percentage_in_computer_architecture')		
            x['percentage_in_mathematics']=request.POST.get('percentage_in_mathematics')		
            x['percentage_in_communication_skills']=request.POST.get('percentage_in_communication_skills')		
            x['how_many_hours_in_a_day_you_can_work']=request.POST.get('how_many_hours_in_a_day_you_can_work')		
            x['Rate_your_logical_quotient']=request.POST.get('Rate_your_logical_quotient')		
            x['How_may_hackathon_have_you_participated']=request.POST.get('How_may_hackathon_have_you_participated')		
            x['Rate_your_coding_skills']=request.POST.get('Rate_your_coding_skills')		
            x['Rate_your_public_speaking']=request.POST.get('Rate_your_public_speaking')		
            x['can_work_long_time_before_system']=request.POST.get('can_work_long_time_before_system')
            x['self_learning_capability']=request.POST.get('self_learning_capability')
            x['which_certifications_do_you_prefer']=request.POST.get('which_certifications_do_you_prefer')
            x['any_talenttests_taken']=request.POST.get('any_talenttests_taken')
            x['scale_your_reading_and_writing_skills']= request.POST.get('scale_your_reading_and_writing_skills')
            x['scale_your_memory_capability_score'] = request.POST.get('scale_your_memory_capability_score')
            x['Interested_subjects'] = request.POST.get('Interested_subjects')
            x['interested_career_area'] = request.POST.get('interested_career_area')
            x['what_do_you_prefer_job_or_higher_studies'] = request.POST.get('what_do_you_prefer_job_or_higher_studies')
            x['type_of_company_you_prefer'] = request.POST.get('type_of_company_you_prefer')
            x['intereaction_with_seniors'] = request.POST.get('intereaction_with_seniors')
            x['do_you_love_games'] = request.POST.get('do_you_love_games')
            x['type_of_books_you_prefer'] = request.POST.get('type_of_books_you_prefer')
            x['most_likely_behaviour'] = request.POST.get('most_likely_behaviour')
            x['what_you_prefer_managemet_or_technical'] = request.POST.get('what_you_prefer_managemet_or_technical')
            x['have_you_ever_worked_with_teams'] = request.POST.get('have_you_ever_worked_with_teams')
            x['Are_you_an_Introvert']= request.POST.get('Are_you_an_Introvert') 
		
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
