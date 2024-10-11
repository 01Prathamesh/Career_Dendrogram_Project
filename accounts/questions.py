from django import forms
subjects = (
    ('--Select--','--Select--'),
    ('Science','Science'),
    ('Mathematics','Mathematics'),
    ('Literature','Literature'),
    ('Arts','Arts'),
    ('History','History'),
    ('Technology','Technology'),
    ('Business','Business'),
)
hobbies = (
    ('--Select--','--Select--'),
    ('Painting', 'Painting'),
    ('Writing', 'Writing'),
    ('Playing sports', 'Playing sports'),
    ('Gaming', 'Gaming'),
    ('Cooking', 'Cooking'),
    ('Volunteering', 'Volunteering'),
    ('Crafting', 'Crafting'),
)

work_preference = (
    ('--Select--','--Select--'),
    ('In a Team', 'In a team'),
    ('Independently', 'Independently'),
    ('A Mix of Both (Independent as well as in a Team)', 'A mix of both'),
)

environment = (
    ('--Select--','--Select--'),
    ('Office', 'Office'),
    ('Outdoors', 'Outdoors'),
    ('Remote', 'Remote'),
    ('Laboratory', 'Laboratory'),
    ('Classroom', 'Classroom'),
)

skill = (
    ('--Select--','--Select--'),
    ('Communication', 'Communication'),
    ('Analytical Thinking', 'Analytical thinking'),
    ('Creativity', 'Creativity'),
    ('Leadership', 'Leadership'),
    ('Technical Skills', 'Technical skills'),
)

technology_comfort = (
    ('--Select--','--Select--'),
    ('Very Comfortable', 'Very comfortable'),
    ('Somewhat Comfortable', 'Somewhat comfortable'),
    ('Not Comfortable', 'Not comfortable'),
)

creativity_importance = (
    ('--Select--','--Select--'),
    ('Very Important', 'Very important'),
    ('Somewhat Important', 'Somewhat important'),
    ('Not Important', 'Not important'),
)

career_importance = (
    ('--Select--','--Select--'),
    ('Job Security', 'Job security'),
    ('High Salary', 'High salary'),
    ('Creativity', 'Creativity'),
    ('Helping Others', 'Helping others'),
    ('Work Life Balance', 'Work-life balance'),
)

age_group = (
    ('--Select--','--Select--'),
    ('Children', 'Children'),
    ('Teenagers', 'Teenagers'),
    ('Adults', 'Adults'),
    ('All Ages', 'All ages'),
)

healthcare_interest = (
    ('--Select--','--Select--'),
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Somewhat', 'Somewhat'),
)

public_speaking = (
    ('--Select--','--Select--'),
    ('Enjoy It', 'I enjoy it'),
    ('Can Manage', 'I can manage'),
    ('Prefer To Avoid', 'I prefer to avoid it'),
)

business_interest = (
    ('--Select--','--Select--'),
    ('Management', 'Management'),
    ('Finance', 'Finance'),
    ('Marketing', 'Marketing'),
    ('Entrepreneurship', 'Entrepreneurship'),
    ('Human Resources', 'Human Resources'),
)

environmental_interest = (
    ('--Select--','--Select--'),
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Somewhat', 'Somewhat'),
)

IT_interest = (
    ('--Select--','--Select--'),
    ('CyberSecurity', 'Cybersecurity'),
    ('Software Development', 'Software Development'),
    ('Networking', 'Networking'),
    ('Database Management', 'Database Management'),
    ('Web Development', 'Web Development'),
)

financial_decisions = (
    ('--Select--','--Select--'),
    ('Analytical Calculated', 'Analytical and calculated'),
    ('Gut Feeling', 'Gut feeling'),
    ('Mix', 'A mix of both'),
)

hands_on_work = (
    ('--Select--','--Select--'),
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Sometimes', 'Sometimes'),
)

arts_interest = (
    ('--Select--','--Select--'),
    ('Visual Arts', 'Visual arts'),
    ('Music', 'Music'),
    ('Literature', 'Literature'),
    ('Theater', 'Theater'),
    ('Dance', 'Dance'),
)

research_interest = (
    ('--Select--','--Select--'),
    ('Love It', 'I love it'),
    ('Can Manage', 'I can manage'),
    ('Prefer Practical', 'I prefer practical work'),
)

entrepreneurship_interest = (
    ('--Select--','--Select--'),
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Maybe', 'Maybe'),
)

learning_style = (
    ('--Select--','--Select--'),
    ('Hands-On', 'Hands-on'),
    ('Visual', 'Visual'),
    ('Auditory', 'Auditory'),
    ('Reading/Writing', 'Reading/Writing'),
)

class Test(forms.Form):
    Which_subjects_did_you_enjoy_most_in_school = forms.ChoiceField(choices=subjects, required=True)
    What_hobbies_do_you_spend_the_most_time_on = forms.ChoiceField(choices=hobbies, required=True)
    How_do_you_prefer_to_work = forms.ChoiceField(choices=work_preference, required=True)
    What_type_of_environment_do_you_thrive_in = forms.ChoiceField(choices=environment, required=True)
    Which_of_the_following_skills_do_you_consider_your_strongest = forms.ChoiceField(choices=skill, required=True)
    How_comfortable_are_you_with_technology = forms.ChoiceField(choices=technology_comfort, required=True)
    How_important_is_creativity_in_your_career_choice = forms.ChoiceField(choices=creativity_importance, required=True)
    What_is_most_important_to_you_in_a_career = forms.ChoiceField(choices=career_importance, required=True)
    Which_age_group_do_you_prefer_to_work_with = forms.ChoiceField(choices=age_group, required=True)
    Are_you_interested_in_healthcare_or_helping_others = forms.ChoiceField(choices=healthcare_interest, required=True)
    How_do_you_feel_about_public_speaking = forms.ChoiceField(choices=public_speaking, required=True)
    What_aspect_of_business_interests_you_the_most = forms.ChoiceField(choices=business_interest, required=True)
    Are_you_passionate_about_environmental_issues = forms.ChoiceField(choices=environmental_interest, required=True)
    Which_area_of_IT_interests_you_the_most = forms.ChoiceField(choices=IT_interest, required=True)
    How_do_you_approach_financial_decisions = forms.ChoiceField(choices=financial_decisions, required=True)
    Do_you_enjoy_hands_on_work = forms.ChoiceField(choices=hands_on_work, required=True)
    Which_area_of_arts_and_culture_fascinates_you = forms.ChoiceField(choices=arts_interest, required=True)
    How_do_you_feel_about_research_and_analysis = forms.ChoiceField(choices=research_interest, required=True)
    Are_you_interested_in_entrepreneurship = forms.ChoiceField(choices=entrepreneurship_interest, required=True)
    Which_of_the_following_best_describes_your_learning_style = forms.ChoiceField(choices=learning_style, required=True)

    def clean(self):
        cleaned_data = super().clean()
        
        for field in self.fields:
            if cleaned_data.get(field) == '--Select--':
                self.add_error(field, '*Please select.')

        return cleaned_data


