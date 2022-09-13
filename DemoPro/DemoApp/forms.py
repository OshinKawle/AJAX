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
'''
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'nameid'}),


            'contents': forms.TextInput(attrs={'class': 'form-control',
                                               'id': 'contentsid'}),
        }
    def clean_name(self):
        all_cleaned_data = super().clean()
        p = all_cleaned_data['name']

        if len(p) < 5 :
            raise forms.ValidationError('Banner Name length should be more than 5')

'''






class CourseForm(forms.ModelForm):
    class Meta:

        model = Course
        fields = '__all__'

class SpecializationForm(forms.ModelForm):
    class Meta:

        model = Specialization
        fields = '__all__'



