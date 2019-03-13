from django import forms
from .models import Student , Major

class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj['major_title']   #페이지상에서 띄어줄 이름 
  

#html에서 사용 , 입력과 수정이 용이
class StudentForm(forms.Form):
    studentID = forms.IntegerField(label="F StudentID")
    name = forms.CharField(label="F name")
    major_id = forms.ModelChoiceField( queryset = Major.objects.all()) #foriegnkey Major에서 참조
    phone = forms.CharField(label="F phone", required = False )
    address = forms.CharField(label="F address", required = False )
    hobby = forms.CharField(label="F hobby", required = False )
    skill = forms.CharField(label="F skill", required = False ) #required = False 널값 허용

    def save(self, commit=True):
        student = Student(**self.cleaned_data)
       # cleaned_data : {'studentID': 600, 'name': '이남기', 'major_id': <Major: 의료IT마케팅>,
       #  'phone': '1111111', 'address': '1234@naver.com', 'hobby': '사진', 'skill': '없음'}  
        if commit:
            student.save()
        return student
