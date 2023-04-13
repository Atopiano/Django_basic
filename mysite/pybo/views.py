from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    # Templates 경로는 C:/projects/mysite/templates
    # 'pybo/question_list.html' -> 'pybo/' 경로를 직접 생성이 필요

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # 아래 create 함수는 Answer 클래스 모델을 가져와 저장할 때 사용하는 save() 랑 동일한 기능
    question.answer_set.create(content=request.POST.get("content"), create_date=timezone.now())
    # a = Answer(question=question, content=request.POST.get("content"), craate_date=timezone.now())
    # a.save()
    return redirect("pybo:detail", question_id=question.id)
