from django.contrib import admin
from .models import Banner,University,Course,Specialization
# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ['b_id', 'name', 'image', 'status', 'created_at','deleted_at', 'updated_at', 'contents']


admin.site.register(Banner, BannerAdmin)


class UniversityAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ['uni_id', 'name', 'logo', 'created_at', 'updated_at', 'contents']


admin.site.register(University, UniversityAdmin)

class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['course_id','uni_id', 'name', 'created_at', 'updated_at', 'contents']


admin.site.register(Course,CourseAdmin)

class SpecializationAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['course_id','uni_id', 'name', 'created_at', 'updated_at', 'contents']


admin.site.register(Specialization,SpecializationAdmin)