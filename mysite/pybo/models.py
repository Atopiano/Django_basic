# 스프링의 @Entity로 Class 생성했던것과 유사함
# 게시판 -> 질문하기, 답변하기
# 질문하기 -> 제목, 내용, 첨부하기, 작성시간, 글쓴이, ??
# 답변하기 -> 내용, 작성시간
# 1:N 구성

from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200) # 문자열 길이를 제한할 때 사용
    content = models.TextField()    # 문자열 제한이 없는 데이터 타입
    create_date = models.DateTimeField() # 날짜와 시간

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()