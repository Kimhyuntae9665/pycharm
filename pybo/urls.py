from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    #템플릿에서 URL 별칭 사용하기
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]