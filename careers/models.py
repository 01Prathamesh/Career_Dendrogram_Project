# from django.db import models
# from django.contrib.auth.models import User

# class TestQuestion(models.Model):
#     text = models.CharField(max_length=255)
#     choices = models.JSONField()  # Store choices as a JSON array

#     def __str__(self):
#         return self.text
    
    
# class UserTestResponse(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
#     selected_option = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.user.username} - {self.question.question_text}"


# class CareerPath(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()

# class Role(models.Model):
#     title = models.CharField(max_length=255)
#     career_path = models.ForeignKey(CareerPath, on_delete=models.CASCADE)
#     prerequisites = models.ManyToManyField('self', blank=True)


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='career_profile')
#     current_role = models.CharField(max_length=100, blank=True)
#     career_goals = models.TextField(blank=True)
#     photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     location = models.CharField(max_length=100, blank=True, null=True)
#     education = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.user.username


# Updated code
from django.db import models
from django.contrib.auth.models import User

# class TestQuestion(models.Model):
#     text = models.CharField(max_length=255)
#     choices = models.JSONField()  # Store choices as a JSON array

#     def __str__(self):
#         return self.text

# class UserTestResponse(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
#     selected_option = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.user.username} - {self.question.text}"

# class CareerPath(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()

#     def __str__(self):
#         return self.title

# class Role(models.Model):
#     title = models.CharField(max_length=255)
#     career_path = models.ForeignKey(CareerPath, on_delete=models.CASCADE)
#     prerequisites = models.ManyToManyField('self', blank=True)

#     def __str__(self):
#         return self.title

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='career_profile')
#     current_role = models.CharField(max_length=100, blank=True)
#     career_goals = models.TextField(blank=True)
#     photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     location = models.CharField(max_length=100, blank=True, null=True)
#     education = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.user.username
