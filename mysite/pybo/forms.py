from django import forms
from .models import Question, Answer

# forms 라이브러리의 ModelForm 상속받아서 사용
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question    # models.py에서 정의한 클래스(모델)
        fields = ["subject", "content"]     # models.py에서 정의한 필드들 (create_data는 제외)
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        }
        labels = {
            'subject': "제목",
            'content': "내용"
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]
        labels = {
            "content" : "답변내용"
        }