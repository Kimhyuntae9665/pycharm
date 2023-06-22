from django.contrib import admin

from .models import Question

# QuestionAdmin 클래스를 생성하고 제목 검색을 위해 search_fields 속성에 subject를 추가 했다
#검색 기능이 추가된 화면 구현
class QuestionAdmin(admin.ModelAdmin):
    search_fields=['subject']

admin.site.register(Question,QuestionAdmin)
