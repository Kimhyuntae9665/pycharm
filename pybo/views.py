from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Question




def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request,'pybo/question_detail.html',context)

def detail(request,question_id):
    #여기서 3번째 question 객체가 question 변수에 들어간다
    question = get_object_or_404(Question,pk=question_id)
    context = {'question':question}
    # 'pybo/question_detail.html'  여기로 context 변수에 Question 모델 갹체를  담아서 보낸다
    return render(request,'pybo/question_detail.html',context)


#답변을 생성한 후 질문 상세 화면을 다시 보여주기 위해 redirect 함수를 사용했다. redirect
#함수는 페이지 이동을 위한 함수이다. pybo:detail 별칭에 해당하는 페이지로 이동하기 위해
#redirect 함수를 사용했다. 그리고 pybo:detail별칭에 해당하는 URL 은 question_id 가 필요하므로
#question.id를 인수로 전달했다.

def answer_create(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),create_date = timezone.now())
    return redirect('pybo:detail',question_id=question.id)