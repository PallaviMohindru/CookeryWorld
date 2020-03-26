from django.shortcuts import render , redirect
from django.contrib import auth
from django.contrib.auth.models import User

def home(request):
    return render(request,'home.html')

def author(request):
    return render(request,'author.html')

def login(request):
    if request.method =='POST':
            if auth.authenticate(username=request.POST["username"], password=request.POST["password"]):
                return redirect('recipeslist')
            else:
                return render(request,'login.html',{'error':'**Username or password Incorrect. Try Again.'})
    else:
        return render(request,'login.html')

def signup(request):
    if request.method =='POST':
        if request.POST['username'] == '' or request.POST['password']== '' or request.POST['cnfpassword'] == '':
            return render(request,'signup.html',{'error':'**Every field is mandatory to signup'})
        if request.POST['password'] == request.POST['cnfpassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{'error':'**User already exists with this username. Please select different username'})
            except User.DoesNotExist:
                User.objects.create_user(username=request.POST['username'], password = request.POST['password'] )
                return render(request,'signup.html',{'signedup':'**User created'})
        else:
            return render(request,'signup.html',{'error':'**Password and Confirm password donot match'})
    else:
        return render(request,'signup.html')
