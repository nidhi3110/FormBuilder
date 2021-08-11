from django.urls import path
from . import views

app_name = "surveys" 

urlpatterns = [
    path('<int:survey_id>/', views.fetchSurvey),
    path('create/', views.createSurvey, name = "create"),
    path('stats/<int:survey_id>/', views.viewStats),
]

