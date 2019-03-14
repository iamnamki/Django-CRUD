from django.shortcuts import render , redirect
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

'''class StudentCreate(CreateView):

    model = Student
    template_name='crud/student_create.html'
    fields = ['studentID','name','major_id','phone','address','hobby','skill']
    
student_create = StudentCreate.as_view()'''

from .forms import StudentForm
def student_create(request):
    if request.method == 'GET': 
        form = StudentForm() #StudentForm객체 생성
    else:
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid(): #유효한 데이터 확인 -> 클린 데이터
            form.save() #폼 저장
            return redirect(reverse("crud:list")) #폼 저장 후 이동할 페이지
    return render(request, 'crud/student_form.html',{'form':form})


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

'''from django.shortcuts import get_object_or_404
def student_edit(request, pk):
    student = get_object_or_404(Student, studentID=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, student)
        if form.is_valid():
            student = form.save(commit=False)
            return redirect('/crud/')
    else:
        form = StudentForm(student)
    return render(request, 'crud/student_form.html', {'form':form})'''




class Studentdelete(DeleteView):
    model = Student
    template_name='crud/student_delete_confirm.html'
    success_url = '/crud/'

student_delete = Studentdelete.as_view()

#Ajax : Major_id로 찾기 ======================================================
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.http import HttpResponse

@csrf_exempt  #Ajax에서 403오류 막기 
def searchData(request):
    id = request.POST['major_id'] #Major_id
    student = Student.objects.get(major_id = id)  
    # print(student.studentID)
    serialize_student = serialize('json', [student, ]) #객체보내기 
    serialize_student = serialize_student.strip('[]') #한건이므로 list없애기 
    # print(serialize_student)
    return HttpResponse(json.dumps(serialize_student), 'appliation/json')  #json.dumps : json파일을 string 으로