from django.shortcuts import render 
from django.urls import reverse
from .models import Student , Major
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView

#기본적인 학생 리스트 보여주기
class StudentListView(ListView):

    model = Student
    template_name='crud/student_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

student_list = StudentListView.as_view()

class StudentCreate(CreateView):

    model = Student
    template_name='crud/student_create.html'
    fields = ['studentID','name','major_id','phone','address','hobby','skill']
    
student_create = StudentCreate.as_view()


class StudentDetail(DetailView):
    model = Student
    template_name='crud/student_detail.html'
    def get_context_data(self, **kwargs):
        context = super(StudentDetail , self).get_context_data(**kwargs)
        return context

student_detail = StudentDetail.as_view()

class StudentEdit(UpdateView):
    model = Student
    template_name='crud/student_edit.html'
    fields = ['studentID','name','major_id','phone','address','hobby','skill']

student_edit = StudentEdit.as_view()


class Studentdelete(DeleteView):
    model = Student
    template_name='crud/student_delete_confirm.html'
    success_url = '/crud/'

student_delete = Studentdelete.as_view()

    