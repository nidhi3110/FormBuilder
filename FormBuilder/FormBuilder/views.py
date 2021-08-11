from django.shortcuts import render
from django.http import HttpResponse
from Surveys.models import Survey
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/") 
def home(request):
    surveyList = Survey.objects.filter(user_id = request.user.id)
    print(surveyList)
    return render(request,'home.html',{'surveyList': surveyList})

def landingPage(request):
    return render(request , 'landingPage.html')