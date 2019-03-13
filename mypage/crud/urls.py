from django.urls import path
from crud.views import StudentListView
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.student_list, name='list'),
    path('create', views.student_create, name='create'),
    path('<pk>/detail', views.student_detail, name='detail'),
    path('<pk>/edit', views.student_edit, name='edit'),
    path('<pk>/delete', views.student_delete, name='delete'),
    #Ajax통신
    path('searchData/', views.searchData, name='search'),
]