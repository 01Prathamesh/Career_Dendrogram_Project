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
from .forms import TestForm
from .models import UserTestResponse, TestQuestion
import requests
import os
from dotenv import load_dotenv


def home(request):
    news_list = fetch_news()
    return render(request, 'accounts/home.html', {'news_list': news_list})

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
        form.error_messages = {
            'invalid_login': 'Incorrect username or password. Please check your credentials and try again.'
        }
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)

    else:
        form = AuthenticationForm()

    return render(request, 'careers/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def start_test(request):
    questions = TestQuestion.objects.all()  # Fetch all questions from the database
    form = TestForm(questions=questions)

    if request.method == 'POST':
        form = TestForm(request.POST, questions=questions)
        if form.is_valid():
            # Collect user answers
            user_answer = get_user_answers(form, questions)

            # Save user responses to the database
            save_user_responses(user_answer, questions, request.user)

            # Store the answers in the session for future use
            request.session['user_answers'] = user_answer

            return redirect('test_results')  # Redirect to the results page
        else:
            messages.error(request, "Please correct the errors below.")  # Show error messages if form is invalid
    
    return render(request, 'start_test.html', {'form': form})


def get_user_answers(form, questions):
    """Collect user answers from the form using question text as the key."""
    return {
        question.text: form.cleaned_data.get(f'question_{question.id}')
        for question in questions
    }

def save_user_responses(user_answer, questions, user):
    """Save the user's responses to the database."""
    for question in questions:
        response = user_answer.get(question.text)
        if response:
            UserTestResponse.objects.create(
                user=user,
                question=question,  # The TestQuestion object
                selected_option=response  # The user's selected answer
            )

def test_results(request):
    user_answers = request.session.get('user_answers')
    if user_answers is None:
        return redirect('start_test')
    
    questions = TestQuestion.objects.all()
    user_responses = get_user_responses(user_answers, questions)
    suggested_career_paths = determine_career_paths(user_answers)

    return render(request, 'test_results.html', {
        'user_answers': user_answers,  # Pass the dictionary of user answers
        'suggested_career_paths': suggested_career_paths,
    })

def get_user_responses(user_answers, questions):
    """Format the user responses for display using question text."""
    return [
        {
            'question_text': question.text,
            'answer': user_answers.get(question.text)
        }
        for question in questions if user_answers.get(question.text)
    ]

def determine_career_paths(user_answers):
    print("User Answers:", user_answers)
    suggested_paths = set()  # Use a set to automatically handle duplicate suggestions
    
    # Define career paths based on user inputs
    paths_mapping = {
        'Which subjects did you enjoy most in school?': {
            'Science': 'Scientist',
            'Mathematics': 'Data Analyst',
            'Literature': 'Author',
            'Arts': 'Graphic Designer',
            'History': 'Historian',
            'Technology': 'Software Developer',
            'Business': 'Entrepreneur',
        },
        'What hobbies do you spend the most time on': {
            'Painting': 'Artist',
            'Writing': 'Writer',
            'Playing sports': 'Sports Coach',
            'Gaming': 'Game Developer',
            'Cooking': 'Chef',
            'Volunteering': 'Social Worker',
            'Crafting': 'Craftsman',
        },
        'How do you prefer to work?': {
            'In a Team': 'Project Manager',
            'Independently': 'Freelancer',
            'A Mix of Both (Independent as well as in a Team)': 'Team Leader',
        },
        'What type of environment do you thrive in?': {
            'Office': 'Corporate Manager',
            'Outdoors': 'Field Engineer',
            'Remote': 'Remote Developer',
            'Laboratory': 'Researcher',
            'Classroom': 'Teacher',
        },
        'Which of the following skills do you consider your strongest?': {
            'Communication': 'Public Relations Specialist',
            'Analytical Thinking': 'Financial Analyst',
            'Creativity': 'Creative Director',
            'Leadership': 'CEO',
            'Technical Skills': 'Software Engineer',
        },
        'How comfortable are you with technology?': {
            'Very Comfortable': 'IT Specialist',
            'Somewhat Comfortable': 'Technical Support',
            'Not Comfortable': 'Customer Service',
        },
        'How important is creativity in your career choice?': {
            'Very Important': 'Graphic Designer',
            'Somewhat Important': 'Marketing Specialist',
            'Not Important': 'Financial Analyst',
        },
        'What is most important to you in a career': {
            'Job Security': 'Government Job',
            'High Salary': 'Investment Banker',
            'Creativity': 'Artist',
            'Helping Others': 'Social Worker',
            'Work-life balance': 'Remote Developer',
        },
        'Which age group do you prefer to work with?': {
            'Children': 'Teacher',
            'Teenagers': 'Youth Counselor',
            'Adults': 'Corporate Manager',
            'All Ages': 'Healthcare Worker',
        },
        'Are you interested in healthcare or helping others?': {
            'Yes': 'Doctor',
            'No': 'Engineer',
            'Somewhat': 'Nurse',
        },
        'How do you feel about public speaking?': {
            'I enjoy it': 'Public Speaker',
            'I can manage': 'Corporate Trainer',
            'I prefer to avoid it': 'Researcher',
        },
        'What aspect of business interests you the most?': {
            'Management': 'Business Consultant',
            'Finance': 'Investment Banker',
            'Marketing': 'Marketing Specialist',
            'Entrepreneurship': 'Startup Founder',
            'Human Resources': 'HR Manager',
        },
        'Are you passionate about environmental issues?': {
            'Yes': 'Environmental Scientist',
            'No': 'Engineer',
            'Somewhat': 'Sustainability Consultant',
        },
        'Which area of IT interests you the most?': {
            'Cybersecurity': 'Cybersecurity Expert',
            'Software Development': 'Software Engineer',
            'Networking': 'Network Engineer',
            'Database Management': 'Database Administrator',
            'Web Development': 'Web Developer',
        },
        'How do you approach financial decisions?': {
            'Analytical and calculated': 'Financial Analyst',
            'Gut feeling': 'Entrepreneur',
            'A mix of both': 'Business Consultant',
        },
        'Do you enjoy hands-on work?': {
            'Yes': 'Engineer',
            'No': 'Software Developer',
            'Sometimes': 'Architect',
        },
        'Which area of arts and culture fascinates you?': {
            'Visual arts': 'Artist',
            'Music': 'Musician',
            'Literature': 'Writer',
            'Theater': 'Actor',
            'Dance': 'Choreographer',
        },
        'How do you feel about research and analysis?': {
            'I love it': 'Research Scientist',
            'I can manage': 'Analyst',
            'I prefer practical work': 'Engineer',
        },
        'Are you interested in entrepreneurship?': {
            'Yes': 'Startup Founder',
            'No': 'Corporate Worker',
            'Maybe': 'Freelancer',
        },
        'Which of the following best describes your learning style?': {
            'Hands-on': 'Engineer',
            'Visual': 'Designer',
            'Auditory': 'Podcaster',
            'Reading/Writing': 'Author',
        },
    }

    # Function to map answers to career suggestions
    def get_career_suggestion(question, response):
        if question in paths_mapping and response != '--Select--':
            return paths_mapping[question].get(response)

    # Iterate through each user response to suggest career paths
    for question, response in user_answers.items():
        career_suggestion = get_career_suggestion(question, response)
        if career_suggestion:
            suggested_paths.add(career_suggestion)

    # Convert set back to list, sort for readability
    sorted_suggested_paths = sorted(list(suggested_paths))
    
    print("Suggested Career Paths:", sorted_suggested_paths)
    return sorted_suggested_paths

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            user = form.save()
            username = user.username
            messages.success(request, f'Registration successful!!! Welcome, {username}. You can now log in.')
            # Redirect to the login page
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
    # Ensure the user profile exists, or create an empty one
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving the form
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})


def career_paths_api(request):
    data = list(CareerPath.objects.values('id', 'name', 'parent_id'))
    return JsonResponse(data, safe=False)

def declaration(request):
    return render(request, 'accounts/declaration.html')

def career_view(request, category):
    template_name = f'careers/options/{category}.html'
    return render(request, template_name)

def fetch_news():
    # Get the NewsAPI key from environment variables
    api_key = os.getenv('NEWS_API_KEY')  # Fetch the API key from the .env file

    if not api_key:
        raise ValueError("API key is missing. Please add it to the .env file.")
    
    url = f'https://newsapi.org/v2/top-headlines?category=business&apiKey={api_key}'

    response = requests.get(url)
    data = response.json()

    # Extract articles from the API response
    if response.status_code == 200:
        return data.get('articles', [])
    else:
        return []

from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import CustomPasswordChangeForm

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Keeps the user logged in after changing password
            messages.success(request, '🎉 Your password was successfully updated! Now you can continue exploring your account.')
            return redirect('profile')  # Redirect back to the profile page
        else:
            messages.error(request, '❌ Oops! Please correct the error(s) below to update your password.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'accounts/change_password.html', {'form': form})

CAREER_PAGES = {
    "art-teacher": "careers/options/art_teacher.html",
    "artist": "careers/options/artist.html",
    "arts": "careers/options/arts.html",
    "author": "careers/options/author.html",
    "chartered-accountant": "careers/options/ca.html",
    "child-psychologist": "careers/options/child_psychologist.html",
    "commerce": "careers/options/commerce.html",
    "conservationist": "careers/options/conservationist.html",
    "content-creator": "careers/options/content_creator.html",
    "corporate-employee": "careers/options/corporate_employee.html",
    "creative-director": "careers/options/creative_director.html",
    "cybersecurity-analyst": "careers/options/cybersecurity_analyst.html",
    "data-analyst": "careers/options/data_analyst.html",
    "engineer": "careers/options/engineering.html",
    "environmental-scientist": "careers/options/environmental_scientist.html",
    "financial-analyst": "careers/options/financial_analyst.html",
    "freelancer": "careers/options/freelancer.html",
    "graphic-designer": "careers/options/graphic_designer.html",
    "healthcare-professional": "careers/options/healthcare_professional.html",
    "manager": "careers/options/manager.html",
    "mechanic": "careers/options/mechanic.html",
    "public-relations-specialist": "careers/options/PR_specialist.html",
    "public-speaker": "careers/options/public_speaker.html",
    "remote-worker": "careers/options/remote_worker.html",
    "research-scientist": "careers/options/research_scientist.html",
    "science": "careers/options/science.html",
    "sports-coach": "careers/options/sports_coach.html",
    "startup-founder": "careers/options/startup_founder.html",
    "vocational-courses": "careers/options/vocational_courses.html",
    "workshop-instructor": "careers/options/workshop_instructor.html",
}

def career_detail(request, career_name):
    """ View function to serve the correct career page based on user input """
    template = CAREER_PAGES.get(career_name.lower())

    if template:
        return render(request, template)
    else:
        return render(request, 'careers/options/career_not_found.html', {'career_name': career_name})

