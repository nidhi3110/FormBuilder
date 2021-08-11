from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import SignUpForm 

# Create your views here.
def signup_view(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

            return redirect('list')

    else:
        form = SignUpForm()

    return render(request,'signup.html', {'form' : form, 'message': ''})

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            print(user)
            return redirect('list')

    else:
        form = AuthenticationForm()

    return render(request,'login.html', {'form' : form, 'message': ''})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landingPage')
