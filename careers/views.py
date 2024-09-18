# from django.shortcuts import render, redirect, get_object_or_404
# from .models import CareerPath, Role
# from .forms import RegistrationForm, UserProfileForm, CareerPathForm, RoleForm
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib.auth.forms import AuthenticationForm
# from .models import UserProfile
# from django.contrib.auth import logout as auth_logout
# from .forms import UserProfileForm 
# from .models import TestQuestion, UserTestResponse
# from .forms import TestForm




# def home(request):
#     return render(request, 'careers/home.html')

# def career_list(request):
#     careers = CareerPath.objects.all()
#     print(careers)  # Debugging statement
#     return render(request, 'careers/career_list.html', {'careers': careers})


# def role_list(request):
#     roles = Role.objects.all()
#     return render(request, 'careers/role_list.html', {'roles': roles})

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = RegistrationForm()
#     return render(request, 'careers/register.html', {'form': form})

# # @login_required
# # def profile(request):
# #     if request.method == 'POST':
# #         form = UserProfileForm(request.POST, instance=request.user.userprofile)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('profile')
# #     else:
# #         form = UserProfileForm(instance=request.user.userprofile)
# #     return render(request, 'accounts/profile.html', {'form': form})

# # @login_required
# # def profile(request):
# #     user = request.user
# #     # Use the correct related_name 'career_profile'
# #     user_profile = get_object_or_404(user.career_profile)
# #     return render(request, 'accounts/profile.html', {'profile': user_profile})


# @login_required
# def profile(request):
#     user = request.user
#     try:
#         user_profile = UserProfile.objects.get(user=user)
#     except UserProfile.DoesNotExist:
#         # Handle the case where the profile does not exist
#         user_profile = None  # or create a new profile, or redirect with a message

#     return render(request, 'accounts/profile.html', {'profile': user_profile})


# @login_required
# def edit_profile(request):
#     # Fetch or create a user profile for the current user
#     user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#     profile = get_object_or_404(UserProfile, user=request.user)
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to the profile page after saving
#     else:
#         form = UserProfileForm(instance=user_profile)

#     return render(request, 'careers/edit_profile.html', {'form': form})


# def add_career_path(request):
#     if request.method == 'POST':
#         form = CareerPathForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('career_list')
#     else:
#         form = CareerPathForm()
#     return render(request, 'careers/add_career_path.html', {'form': form})

# def edit_career_path(request, pk):
#     career_path = get_object_or_404(CareerPath, pk=pk)
#     if request.method == 'POST':
#         form = CareerPathForm(request.POST, instance=career_path)
#         if form.is_valid():
#             form.save()
#             return redirect('career_list')
#     else:
#         form = CareerPathForm(instance=career_path)
#     return render(request, 'careers/edit_career_path.html', {'form': form})

# def delete_career_path(request, pk):
#     career_path = get_object_or_404(CareerPath, pk=pk)
#     if request.method == 'POST':
#         career_path.delete()
#         return redirect('career_list')  # Corrected the redirect name
#     return render(request, 'careers/delete_career_path.html', {'career_path': career_path})

# def add_role(request):
#     if request.method == 'POST':
#         form = RoleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('role_list')
#     else:
#         form = RoleForm()
#     return render(request, 'careers/add_role.html', {'form': form})

# def edit_role(request, pk):
#     role = get_object_or_404(Role, pk=pk)
#     if request.method == 'POST':
#         form = RoleForm(request.POST, instance=role)
#         if form.is_valid():
#             form.save()
#             return redirect('role_list')
#     else:
#         form = RoleForm(instance=role)
#     return render(request, 'careers/edit_role.html', {'form': form})

# def delete_role(request, pk):
#     role = get_object_or_404(Role, pk=pk)
#     if request.method == 'POST':
#         role.delete()
#         return redirect('role_list')
#     return render(request, 'careers/delete_role.html', {'role': role})

# def career_paths_data(request):
#     career_paths = CareerPath.objects.all()
#     data = {
#         'name': 'Career Paths',
#         'children': [
#             {
#                 'name': career.title,
#                 'children': [
#                     {'name': role.title} for role in Role.objects.filter(career_path=career)
#                 ]
#             }
#             for career in career_paths
#         ]
#     }
#     return JsonResponse(data)

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('home')  # Redirect to the home page or another page
#     else:
#         form = AuthenticationForm()
#     return render(request, 'careers/login.html', {'form': form})

# def logout_view(request):
#     auth_logout(request)  # Log out the user
#     return redirect('home')  # Redirect to the home page or any other page

# def dendrogram(request):
#     return render(request, 'careers/dendrogram.html')

# def career_paths_api(request):
#     data = list(CareerPath.objects.values('id', 'name', 'parent_id'))
#     return JsonResponse(data, safe=False)


# def start_test(request):
#     if request.method == 'POST':
#         form = TestForm(request.POST, questions=TestQuestion.objects.all())
#         if form.is_valid():
#             for question in TestQuestion.objects.all():
#                 selected_option = form.cleaned_data[f'question_{question.id}']
#                 UserTestResponse.objects.create(
#                     user=request.user,
#                     question=question,
#                     selected_option=selected_option
#                 )
#             return redirect('test_results') 
#     else:
#         questions = TestQuestion.objects.all()
#         form = TestForm(questions=questions)
    
#     return render(request, 'start_test.html', {'form': form})


    
# def test_results(request):
#     # Add logic to handle test results here
#     return render(request, 'test_results.html')


# Updated Code
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import CareerPath, Role, UserProfile, TestQuestion, UserTestResponse
from .forms import RegistrationForm, UserProfileForm, CareerPathForm, RoleForm, TestForm

# def home(request):
#     return render(request, 'careers/home.html')

# def career_list(request):
#     careers = CareerPath.objects.all()
#     return render(request, 'careers/career_list.html', {'careers': careers})

def dendrogram(request):
    return render(request, 'careers/dendrogram.html')

# def role_list(request):
#     roles = Role.objects.all()
#     return render(request, 'careers/role_list.html', {'roles': roles})

# def add_career_path(request):
#     if request.method == 'POST':
#         form = CareerPathForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('career_list')
#     else:
#         form = CareerPathForm()
#     return render(request, 'careers/add_career_path.html', {'form': form})

#  def add_role(request):
#     if request.method == 'POST':
#         form = RoleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('role_list')
#     else:
#         form = RoleForm()
#     return render(request, 'careers/add_role.html', {'form': form})

# def edit_career_path(request, pk):
#     career_path = get_object_or_404(CareerPath, pk=pk)
#     if request.method == 'POST':
#         form = CareerPathForm(request.POST, instance=career_path)
#         if form.is_valid():
#             form.save()
#             return redirect('career_list')
#     else:
#         form = CareerPathForm(instance=career_path)
#     return render(request, 'careers/edit_career_path.html', {'form': form})

# def delete_career_path(request, pk):
#     career_path = get_object_or_404(CareerPath, pk=pk)
#     if request.method == 'POST':
#         career_path.delete()
#         return redirect('career_list')
#     return render(request, 'careers/delete_career_path.html', {'career_path': career_path})

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

# def edit_role(request, pk):
#     role = get_object_or_404(Role, pk=pk)
#     if request.method == 'POST':
#         form = RoleForm(request.POST, instance=role)
#         if form.is_valid():
#             form.save()
#             return redirect('role_list')
#     else:
#         form = RoleForm(instance=role)
#     return render(request, 'careers/edit_role.html', {'form': form})

# def delete_role(request, pk):
#     role = get_object_or_404(Role, pk=pk)
#     if request.method == 'POST':
#         role.delete()
#         return redirect('role_list')
#     return render(request, 'careers/delete_role.html', {'role': role})

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'careers/login.html', {'form': form})

# def logout_view(request):
#     auth_logout(request)
#     return redirect('home')

# def start_test(request):
#     if request.method == 'POST':
#         form = TestForm(request.POST, questions=TestQuestion.objects.all())
#         if form.is_valid():
#             for question in TestQuestion.objects.all():
#                 selected_option = form.cleaned_data.get(f'question_{question.id}')
#                 if selected_option:
#                     UserTestResponse.objects.create(
#                         user=request.user,
#                         question=question,
#                         selected_option=selected_option
#                     )
#             return redirect('test_results')
#     else:
#         questions = TestQuestion.objects.all()
#         form = TestForm(questions=questions)
#     return render(request, 'start_test.html', {'form': form})

# def test_results(request):
#     # Implement logic to handle and display test results
#     return render(request, 'test_results.html')

# @login_required
# def edit_profile(request):
#     user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = UserProfileForm(instance=user_profile)
#     return render(request, 'careers/edit_profile.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = RegistrationForm()
#     return render(request, 'careers/register.html', {'form': form})

# @login_required
# def profile(request):
#     try:
#         user_profile = UserProfile.objects.get(user=request.user)
#     except UserProfile.DoesNotExist:
#         user_profile = None  # Or handle appropriately
#     return render(request, 'accounts/profile.html', {'profile': user_profile})



def career_paths_api(request):
    data = list(CareerPath.objects.values('id', 'name', 'parent_id'))
    return JsonResponse(data, safe=False)

