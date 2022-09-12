from django import forms
from .models import Banner,University,Course,Specialization


class BannerForm(forms.ModelForm):
    class Meta:

        model = Banner
        fields = '__all__'

class UniversityForm(forms.ModelForm):
    class Meta:

        model = University
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:

        model = Course
        fields = '__all__'

class SpecializationForm(forms.ModelForm):
    class Meta:

        model = Specialization
        fields = '__all__'



