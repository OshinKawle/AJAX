
from django.urls import path
from . import views


urlpatterns=[
    path('app/',views.banner,name='banner'),
    path('show/',views.show,name='show'),
    path('delete/<int:i>/',views.delete,name='del'),
    path('update/<int:i>/',views.update,name='upd'),
    path('adduni/',views.university,name='uni'),
    path('showuni/',views.showUniversity,name='showUni'),
    path('del/<int:i>/', views.deleteUni, name='del_uni'),
    path('upd/<int:i>/', views.updateUni, name='upd_uni'),
    path('addcourse/',views.course),
    path('special/',views.specialization),
    #path('drop/',views.load_courses,name='data_url')
    #path('edit/<int:pk>/',views.banner_edit)
]
