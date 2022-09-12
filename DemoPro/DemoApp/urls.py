
from django.urls import path
from . import views


urlpatterns=[
    path('app/',views.banner),
    path('show/',views.show,name='show'),
    path('delete/<int:i>/',views.delete,name='del'),
    path('update/<int:i>/',views.update,name='upd'),
    path('adduni/',views.university),
    path('addcourse/',views.course),
    path('special/',views.specialization,name='data_url'),
    #path('drop/',views.load_courses,name='data_url')
    #path('edit/<int:pk>/',views.banner_edit)
]
