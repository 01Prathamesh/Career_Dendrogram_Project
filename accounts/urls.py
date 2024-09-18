# # accounts/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('profile/', views.profile, name='profile'),
#     # Add other URLs if needed, e.g., password change, reset
# ]

# Updated Code
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URL pattern for the user profile page
    path('', views.home, name='home'),
    path('career_list/', views.career_list, name='career_list'),
    path('dendrogram/', views.dendrogram, name='dendrogram'),
    path('roles/', views.role_list, name='role_list'),
    path('career_paths/add/', views.add_career_path, name='add_career_path'),
    path('career_paths/edit/<int:pk>/', views.edit_career_path, name='edit_career_path'),
    path('career_paths/delete/<int:pk>/', views.delete_career_path, name='delete_career_path'),
    path('roles/add/', views.add_role, name='add_role'),
    path('roles/edit/<int:pk>/', views.edit_role, name='edit_role'),
    path('roles/delete/<int:pk>/', views.delete_role, name='delete_role'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('start_test/', views.start_test, name='start_test'),
    path('test-results/', views.test_results, name='test_results'),
    path('profile/', views.profile, name='profile'),
    path('profile/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    
    # URL pattern for user registration
    path('register/', views.register, name='register'),
    
    path('api/career_paths/', views.career_paths_data, name='career_paths_data'),
    # URL pattern for updating user profile
    # This is redundant if `profile` is handling both viewing and updating
    # path('edit_profile/', views.profile_view, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
