from hashlib import new
from urllib import request
from django.shortcuts import render,redirect
from question.models import Question, Answer, Video, Emails,Websites
from django.core.paginator import Paginator
import random

from django.http.response import HttpResponseRedirect
from django.urls import reverse

from .forms.type_form import QuestionType
from .forms.answer_form import CHOICES

 
def display_images(request): 
  
    # getting all the objects of hotel. 
    allimages = Question.objects.all()  
    num = 1
    return render(request, 'deneme.html',{'num' : num})
def yeni(request, soru):
    soru = 'email/' + soru
    return render(request, soru, {'soru': soru})
def done(request):

    return render(request, 'done.html')

def info_view(request):

    if request.method == 'POST':
        qtype = request.POST.get('test')
        #print(qtype)

        return HttpResponseRedirect(reverse('questions', args=[qtype]))
    
    return render(request, 'info.html')


def questions(request,qtype):


    if request.method == 'POST':
        c_answer = request.POST.get('c_answer')
        if c_answer == None:
            c_answer = "None of them"
        answer = request.POST.get('answer')

        if c_answer == answer:
            result = 'True'
        else:
            result = 'False'

        return HttpResponseRedirect(reverse('results', args=[result]))


    if qtype == 'email':
        question = Emails.objects.all()
    else:
        question = Websites.objects.all()

     
    if qtype in request.session:
        if len(request.session[qtype]) == 14: ##emails lenght./////////////
            print("flushed!")
            request.session.flush()
            return HttpResponseRedirect(reverse('information'))


        #in a func ////////////
        
        sel_1 = random.choice(question).ID-1
        while sel_1 in request.session[qtype]:
            sel_1 = random.choice(question).ID-1

        print(f"Added q_number = {sel_1}")    
        request.session[qtype].append(sel_1)


        sel_2 = random.choice(question).ID-1
        while sel_2 in request.session[qtype]:
            sel_2 = random.choice(question).ID-1
        
        print(f"Added q_number = {sel_2}")
        request.session[qtype].append(sel_2)

        print(request.session[qtype])
       

        selection = (question[sel_1], question[sel_2])

    else: 
        selection = random.choices(question, k=2)
        while selection[0] == selection[1]:
            selection = random.choices(question, k=2)
        request.session[qtype] = [selection[0].ID-1]
        request.session[qtype].append(selection[1].ID-1)

        print(f"List has created with keys: {selection[0].ID} {selection[1].ID}")
    
    #del request.session[qtype]
    
    request.session.modified = True


    if selection[0].Phishing == True and selection[1].Phishing == True:
        answer = "Both of them"
    elif selection[0].Phishing == True and selection[1].Phishing == False:
        answer = "Only left one"
    elif selection[0].Phishing == False and selection[1].Phishing == True:
        answer = "Only right one"
    elif selection[0].Phishing == False and selection[1].Phishing == False:
        answer = "None of them"

    print(f"CEVAPPP: {answer}")

    #tek paket ////////////////////
    sel_html_1 = selection[0].Html_Name
    sel_html_2 = selection[1].Html_Name
    sel_html = (sel_html_1, sel_html_2)


    sel_url_1 = selection[0].URL.replace("/","^")
    sel_url_2 = selection[1].URL.replace("/","^")
    sel_url = (sel_url_1, sel_url_2)
    
    
    context = {
        'selection' : sel_html,
        'url':sel_url,
        'answer':answer,
        'qtype':qtype
    }




    return render(request, 'quiz.html', context)

 
def body(request, email):
    email = "email/" + email
    
    return render(request, email, {'email': email})


def tekresult(request, result):

    if result == 'True':
        return render(request, 'result_true.html')
    else:
        return render(request, 'result_false.html')

def navbar(request, url):

    urlfix = url.replace("^", "/")

    return render(request, 'navbar.html', {'url' : urlfix})


