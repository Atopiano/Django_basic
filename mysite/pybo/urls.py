from django.urls import path
from . import views

app_name = "pybo"

urlpatterns = [
    # localhost:8000/pybo 주소의 루트를 의미함
    path("", views.index, name="index"),

    # 게시글 제목의 a 태그 href 속성에 해당하는 동적 URL 매핑
    path("<int:question_id>", views.detail, name="detail"),

    # 답변 등록에 대한 URL 매핑
    path("answer/create/<int:question_id>/", views.answer_create, name="answer_create")
]