from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return render(request,'home',{'auth':"you are already logged in"})

    if request.method == "POST":
        #create User
        if request.POST['password1'] == request.POST['password2']:
            try:
                testUser = User.objects.get(username = request.POST['username'])
                return render(request,'accounts/signup.html', {'error': 'Username has already been taken'})

            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'], email = request.POST['email'])
                login(request, user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html', {'error': 'Passwords didn\'t match'})
    else:
        return render(request,'accounts/signup.html')


def loginView(request):
    if request.user.is_authenticated:
        return render(request,'games/home.html',{'auth':"you are already logged in"})

    if request.method == "POST":
        request.POST['password']
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            #redirect to success page
            return redirect('home')

        else:
            return render(request,'accounts/login.html',{'error' : 'The Username and password didn\'t match' })
    else:
        return render(request,'accounts/login.html')


def logoutView(request):
    print("TESTIIIING")
    if request.method == "POST":
        logout(request)
        return redirect('home')
