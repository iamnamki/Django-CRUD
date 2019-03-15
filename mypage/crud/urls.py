from django.urls import path
from crud.views import StudentListView
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.student_list, name='list'),
    path('stu', views.student_list, name='slist'),
    path('maj', views.major_list, name='mlist'),
    path('screate', views.screate, name='screate'),
    path('mcreate', views.mcreate, name='mcreate'),
    path('<pk>/detail', views.student_detail, name='detail'),
    path('<pk>/sedit', views.sedit, name='sedit'),
    path('<pk>/medit', views.medit, name='medit'),
    path('<pk>/sdelete', views.sdelete, name='sdelete'),
    path('<pk>/mdelete', views.mdelete, name='mdelete'),
    #Ajax통신
    path('searchData/', views.searchData, name='search'),
    #Fileupload
    path('upload/',views.simple_upload, name ='upload'),
]