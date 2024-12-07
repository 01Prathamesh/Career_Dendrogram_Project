# admin.py (in the 'accounts' app)

from django.contrib import admin
from .models import UserProfile, CareerPath, Role, TestQuestion, UserTestResponse

# Admin configuration for UserProfile model
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'date_of_birth', 'location', 'education_qualification', 'current_role')
    search_fields = ('user__username', 'name', 'location')
    list_filter = ('location', 'education_qualification')
    ordering = ('user__username',)

# Admin configuration for CareerPath model
class CareerPathAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

# Admin configuration for Role model
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'career_path')
    search_fields = ('title',)

# # Admin configuration for TestQuestion model
# class TestQuestionAdmin(admin.ModelAdmin):
#     list_display = ('text', 'choices_display')
#     search_fields = ('text',)

#     # Custom method to display choices
#     def choices_display(self, obj):
#         return ', '.join([f"{choice}" for choice in obj.choices])
#     choices_display.short_description = 'Choices'

class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'choices_display')
    search_fields = ('text',)

    # Custom method to display choices
    def choices_display(self, obj):
        # Ensure obj.choices is a list and not empty
        if isinstance(obj.choices, list) and obj.choices:
            return ', '.join([str(choice) for choice in obj.choices])
        return 'No choices available'  # Display a fallback message if choices are empty or not a list
    choices_display.short_description = 'Choices'

# Admin configuration for UserTestResponse model
class UserTestResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'selected_option')
    search_fields = ('user__username', 'question__text')

# Register the models with their corresponding admin classes
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CareerPath, CareerPathAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(TestQuestion, TestQuestionAdmin)
admin.site.register(UserTestResponse, UserTestResponseAdmin)
