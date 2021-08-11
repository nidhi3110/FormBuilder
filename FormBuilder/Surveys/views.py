from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Survey,SurveyData
from django.contrib.auth.models import User
from .forms import createSurveyForm, surveyForm
from django.contrib.auth.decorators import login_required


def fetchSurvey(request,survey_id):

    SurveyExists = Survey.objects.filter(pk =  survey_id).exists()

    if not SurveyExists :
        message = "Survey Doesnot Exist"
        return render(request,'errorPage.html',{'message' : message})

    surveyDetail = Survey.objects.get(pk =  survey_id)
    surveyOwner = User.objects.get(pk = surveyDetail.user_id)

    if request.method == "POST":
        form = surveyForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.save(commit = False)
            data.user_id = surveyOwner.id
            data.survey_id = survey_id
            data.save()

            messages.success(request, 'Form Submitted Succesfully!!')
            form = surveyForm()
    else:
        form = surveyForm()

    return render(request,'survey.html',{'form': form, 'survey': surveyDetail,'surveyOwner' : surveyOwner})

@login_required(login_url="/accounts/login/") 
def createSurvey(request):
    
    if request.method == "POST":
        form = createSurveyForm(request.POST)
        if form.is_valid():
            data = form.save(commit = False)
            data.user_id = request.user.id
            data.save()

            messages.success(request, 'Survey Created Succesfully!!')

    else:
        form = createSurveyForm()

    return render(request,'create.html',{'form' : form})

@login_required(login_url="/accounts/login/") 
def viewStats(request,survey_id):

    data = SurveyData.objects.all()

    return render(request,'stats.html',{'data' : data})

# @login_required(login_url="/accounts/login/")
# def updateSurvey(request,Survey_id=0):

#     msg = "" 

#     if request.method == 'POST':
#         if Survey_id:
#             user = request.user.id
#             currSurvey = Survey.objects.get(pk=Survey_id)
#             Survey_owner = currSurvey.user_id

#             if user != Survey_owner:
#                 message = "Unauthorised access"
#                 return render(request,'errorPage.html',{'message' : message})

#             form = createSurveyForm(request.POST,request.FILES,instance=currSurvey)

#             if form.is_valid():
#                 form.save()

#                 messages.success(request, 'Survey Updated Succesfully!!')

#         else:
#             form = createSurveyForm(request.POST,request.FILES)
#             print(form)
#             if form.is_valid():
#                 data = form.save(commit = False)
#                 data.user_id = request.user.id
#                 data.save()

#                 messages.success(request, 'Survey Created Succesfully!!')

#     else:
#         if Survey_id:
#             user = request.user.id
#             currSurvey = Survey.objects.get(pk=Survey_id)
#             Survey_owner = currSurvey.user_id

#             if user != Survey_owner:
#                 message = "Unauthorised access"
#                 return render(request,'errorPage.html',{'message' : message})

#             form = createSurveyForm(instance = currSurvey)

#         else:
#             form = createSurveyForm()

#     return render(request,'update.html',{'form' : form, 'id' : Survey_id})

# def deleteSurvey(request):
#     return redirect('list')