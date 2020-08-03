from django import forms
from .models import Post, CodingSkill, AcademicObject, AchievementModel, InterestModel

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class CodingForm(forms.ModelForm):
    class Meta:
        model = CodingSkill
        fields = ('skill', 'proficiency')

class AcademicForm(forms.ModelForm):
    class Meta:
        model = AcademicObject
        fields = ('institution', 'details', 'gradYear')

class AchievementForm(forms.ModelForm):
    class Meta:
        model = AchievementModel
        fields = ('label', 'year', 'month')

class InterestForm(forms.ModelForm):
    class Meta:
        model = InterestModel
        fields = ('title', 'details')
