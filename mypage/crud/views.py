from django.shortcuts import render , redirect
from django.urls import reverse
from .models import Student , Major
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView

#기본적인 학생 리스트 보여주기
class MajorListView(ListView):
    model = Major
    template_name = 'crud/major_list.html'
    paginate_by=5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context
    

major_list = MajorListView.as_view()

class StudentListView(ListView):

    model = Student
    template_name='crud/student_list.html'
    paginate_by=5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context

student_list = StudentListView.as_view()

class StudentCreate(CreateView):

    model = Student
    template_name='crud/create.html'
    fields = ['studentID','name','major_id','phone','address','hobby','skill']
    
screate = StudentCreate.as_view()

class MajorCreate(CreateView):

    model = Major
    template_name='crud/create.html'
    fields = ['major_id','major_title']
    
mcreate = MajorCreate.as_view()

'''from .forms import StudentForm
def screate(request):
    if request.method == 'GET': 
        form = StudentForm() #StudentForm객체 생성
    else:
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid(): #유효한 데이터 확인 -> 클린 데이터
            form.save() #폼 저장
            return redirect(reverse("crud:slist")) #폼 저장 후 이동할 페이지
    return render(request, 'crud/form.html',{'form':form})'''

class StudentDetail(DetailView):
    model = Student
    template_name='crud/student_detail.html'
    def get_context_data(self, **kwargs):
        context = super(StudentDetail , self).get_context_data(**kwargs)
        return context

student_detail = StudentDetail.as_view()

class StudentEdit(UpdateView):
    model = Student
    template_name='crud/edit.html'
    fields = ['studentID','name','major_id','phone','address','hobby','skill']

sedit = StudentEdit.as_view()

class MajorEdit(UpdateView):
    model = Major
    template_name='crud/edit.html'
    fields = ['major_id','major_title']

medit = MajorEdit.as_view()

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
    template_name='crud/delete_confirm.html'
    success_url = '/crud/'
    

sdelete = Studentdelete.as_view()

class Majordelete(DeleteView):
    model = Major
    template_name='crud/confirm.html'
    success_url = '/crud/'

mdelete = Majordelete.as_view()

#Ajax : Major_id로 찾기 ======================================================
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.http import HttpResponse

@csrf_exempt  #Ajax에서 403오류 막기 
def searchData(request):
    info = request.POST['student_info'] #Major_id
    student1 = Student.objects.filter( name__contains= info )
    student2 = Student.objects.filter( studentID__contains= info )

    students = student1 | student2 

    #['studentID','name','major_id','phone','address','hobby','skill']
    #serialize_student = serialize('json', [student, ]) #객체보내기 
    #serialize_student = serialize('json', student) #객체보내기 
    #serialize_student = serialize_student.strip('[]') #한건이므로 list없애기 
    #print(serialize_student)
    #return HttpResponse(json.dumps(serialize_student), 'appliation/json')  
    #json.dumps : json파일을 string 으로
    return render(request, 'crud/student_list2.html', {'student_list':students})

#FileUpload ----------------
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    if request.method == 'POST' and request.FILES['uploadfile']:
        uploadfile = request.FILES['uploadfile']
        fs = FileSystemStorage()
        filename = fs.save(uploadfile.name, uploadfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'crud/student_list.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'crud/student_list.html')