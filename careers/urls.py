# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views
# from .views import logout_view, profile, edit_profile
# from .views import start_test


# urlpatterns = [
#     path('', views.home, name='home'),
#     path('career_list/', views.career_list, name='career_list'),
#     path('dendrogram/', views.dendrogram, name='dendrogram'),
#     path('roles/', views.role_list, name='role_list'),
#     path('register/', views.register, name='register'),
#     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('profile/', views.profile, name='profile'),
#     path('logout/', logout_view, name='logout'),
#     path('edit-profile/', edit_profile, name='edit_profile'),
    
#     # Career paths
#     path('career_paths/add/', views.add_career_path, name='add_career_path'),
#     path('career_paths/edit/<int:pk>/', views.edit_career_path, name='edit_career_path'),
#     path('career_paths/delete/<int:pk>/', views.delete_career_path, name='delete_career_path'),
    
#     # Roles
#     path('roles/add/', views.add_role, name='add_role'),
#     path('roles/edit/<int:pk>/', views.edit_role, name='edit_role'),
#     path('roles/delete/<int:pk>/', views.delete_role, name='delete_role'),
    
#     # API endpoints
#     path('api/career_paths/', views.career_paths_data, name='career_paths_data'),

#     #Test
#     path('start_test/', start_test, name='start_test'),
#     path('test-results/', views.test_results, name='test_results'),

# ]

# Updated code.
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home and Career Paths
    # path('', views.home, name='home'),
    # path('career_list/', views.career_list, name='career_list'),
    # path('dendrogram/', views.dendrogram, name='dendrogram'),

    # Roles
    # path('roles/', views.role_list, name='role_list'),

    # User Authentication
    # path('register/', views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('profile/', views.profile, name='profile'),
    # path('edit-profile/', views.edit_profile, name='edit_profile'),

    # Career Paths Management
    # path('career_paths/add/', views.add_career_path, name='add_career_path'),
    # path('career_paths/edit/<int:pk>/', views.edit_career_path, name='edit_career_path'),
    # path('career_paths/delete/<int:pk>/', views.delete_career_path, name='delete_career_path'),

    # Roles Management
    # path('roles/add/', views.add_role, name='add_role'),
    # path('roles/edit/<int:pk>/', views.edit_role, name='edit_role'),
    # path('roles/delete/<int:pk>/', views.delete_role, name='delete_role'),

    # API Endpoints
    # path('api/career_paths/', views.career_paths_data, name='career_paths_data'),

    # Testing
    # path('start_test/', views.start_test, name='start_test'),
    # path('test-results/', views.test_results, name='test_results'),
]
