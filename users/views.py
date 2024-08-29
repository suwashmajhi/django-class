from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    return render(request,'login.html')

def homepage(request):
    return render(request,'homepage.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)

        user = authenticate(username = username, password = password)
        if user is not None:
            return render(request,'homepage.html')
        else:
            return render(request,'login.html',{'error': 'User or password in incorrect !!!'})
        
    

    return render(request,'login.html')
    
    
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        passowrd = request.POST['password']
        passowrd2 = request.POST['password2']
        if passowrd == passowrd2:
            user = User.objects.create_user(first_name = first_name, last_name = last_name,email = email, username=email, password = passowrd)
            user.save()
            return render(request,'signup.html',{"message":"User created Successfully!!!"})
    
        else:
            return render(request,'signup.html',{"error":"Password didn't match !!!"})
       
    return render(request,'signup.html')