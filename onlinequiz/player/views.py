from django.shortcuts import render,redirect
from question.models import Question
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.




@login_required
def quizhome(request):
    return render(request,'home.html')

@login_required
def sci_level(request):
    return render(request,'sci_level.html')

@login_required
def hist_level(request):
    return render(request,'histlevel.html')
@login_required
def sl1(request):
    return render(request,'scil1.html')

def display_questions(request):
    if request.method == 'POST':
        
        questions=Question.objects.filter(topic='Science',level='Level-1')
        
        print("questb",questions)
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer ==  request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
            print(score)
     
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'total':total,
            'question':questions
        }
        return render(request,'score.html',context)
    else:
        questions=Question.objects.filter(topic='Science',level='Level-1')
        context = {
            'questions':questions
        }
        return render(request,'scil1.html',context)   

    

def sciencel2(request):
    if request.method == 'POST':
        questions=Question.objects.filter(level='Level-2', topic='Science')
        score=0
        wrong=0
        correct=0
        total=0
        
        for q in questions:
            total+=1

            
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer ==  request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
            print(score)
     
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'total':total,
            'question':questions
           
        }
        return render(request,'score.html',context)
    else:
        questions=Question.objects.filter(level='Level-2', topic='Science')
        context = {
            'questions':questions
        }
        return render(request,'scil1.html',context)
    

def sciencel3(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Question.objects.filter(level='Level-3', topic='Science')
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer ==  request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
            print(score)
     
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'total':total,
            'question':questions
        }
        return render(request,'score.html',context)
    else:
        questions=Question.objects.filter(level='Level-3', topic='Science')
        context = {
            'questions':questions
        }
        return render(request,'scil1.html',context)


def historyl1(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Question.objects.filter(level='Level-1', topic='History')
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer ==  request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
            print(score)
     
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'total':total,
            'question':questions
        }
        return render(request,'score.html',context)
    else:
        questions=Question.objects.filter(level='Level-1', topic='History')
        context = {
            'questions':questions
        }
        return render(request,'scil1.html',context)  




def historyl2(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Question.objects.filter(level='Level-2', topic='History')
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer ==  request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
            print(score)
     
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'total':total,
            'question':questions
        }
        return render(request,'score.html',context)
    else:
        questions=Question.objects.filter(level='Level-2', topic='History')
        context = {
            'questions':questions
        }
        return render(request,'scil1.html',context)  

def historyl3(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Question.objects.filter(level='Level-3', topic='History')
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer ==  request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
            print(score)
     
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'total':total,
            'question':questions
        
        }
        return render(request,'score.html',context)
    else:
        questions=Question.objects.filter(level='Level-3', topic='History')
        context = {
            'questions':questions
        }
        return render(request,'scil1.html',context)  
@login_required
def display_score(request,score,questions):
  
    context = {'score': score}
    return render(request, 'score.html', context)
