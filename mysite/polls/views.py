from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question

def save(request, question_id):
    q = request.POST['q']
    question = Question.objects.get(id=question_id)
    question.question_text = q
    question.save()
    return HttpResponse("수정 완료")

def edit(request, question_id):
    q = Question.objects.get(id = question_id)

    return render(
        request, 'polls/edit.html', {'q':q}
    )

def index(request):
    questions = Question.objects.all()
    return render(
        request,
        'polls/index.html',
        {'question':questions})


    choices = q.choice_set.all()

    print(q.question_text)
    print(choices[0].choice_text)
    print(choices[1].choice_text)
    print(choices[2].choice_text)



    #return HttpResponse('polls index')




def detail(request, question_id): # 질문 상세 페이지
    q = Question.objects.get(id = question_id) # 조건에 맞는 데이터 1개 조회
    c = q.choice_set.all()
    #choice = ''
    #for a in c:
    #choice += a.choice_text

                # request 템플릿 커넥스트(데이터/모델)
    return render(request, 'polls/detail.html', {'question':q.question_text, 'num':q.id,'choice':c})

    #return HttpResponse(q.question_text + '<br>' + choice)



def detail2(request, num1, num2):
    return HttpResponse(num1 + num2)


def results(request, question_id): # 투표 결과 페이지
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id) #실제투표하는 작업


def vote(request, question_id): # 투표 페이지

    try:
        select = request.POST['select']

        q = Question.objects.get(id = question_id)
        c = q.choice_set.get(id=select)
        c.votes += 1
        c.save()

        print(select)

    except:
        pass

    return render(
        request,
        'polls/result.html',
        {'q':q}
    )


    return HttpResponse("ok")