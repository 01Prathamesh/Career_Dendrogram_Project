# # accounts/models.py

# from django.db import models
# from django.contrib.auth.models import User

# # class UserProfile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account_profile')
# #     bio = models.TextField(blank=True)
# #     location = models.CharField(max_length=100, blank=True)

# #     def __str__(self):
# #         return self.user.username

# # class UserProfile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     photo = models.ImageField(upload_to='profile_photos/', default='profile_photos/default-profile.png')
# #     date_of_birth = models.DateField(null=True, blank=True)
# #     location = models.CharField(max_length=100, blank=True)
# #     education = models.TextField(blank=True)  # Use TextField for qualifications
    
# #     def __str__(self):
# #         return self.user.username

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     location = models.CharField(max_length=100, blank=True)
#     qualification = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.user.username

# Updated Code
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='photo', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    education_qualification = models.CharField(max_length=100, blank=True)
    current_role = models.CharField(max_length=100, blank=True)
    career_goals = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class CareerPath(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Role(models.Model):
    title = models.CharField(max_length=255)
    career_path = models.ForeignKey(CareerPath, on_delete=models.CASCADE)
    prerequisites = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.title
    
class TestQuestion(models.Model):
    text = models.CharField(max_length=255)
    choices = models.JSONField()  # Store choices as a JSON array

    def __str__(self):
        return self.text

class UserTestResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.question.text}"
