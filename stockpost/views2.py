from django.contrib import messages
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate



# Handles Sign-Up
def handleSignup(request):
        
        if request.method == 'POST':

            name = request.POST['name']
            mail = request.POST['email']
            password = request.POST['password']
            confirmPassword = request.POST['confirmPassword']

            #Basic Checks
            check = User.objects.filter(email = mail).exists() 
            if (check):
                messages.warning(request, 'account already exists')

            elif (password != confirmPassword):
                messages.warning(request, "Passwords don't match")

            elif (len(password) < 5):
                messages.warning(request, 'Your passsword is too short')

            else:       
                #Create User
                myuser = User.objects.create_user(name, mail, password)
                myuser.save()
                
                #Authenticating User
                us = authenticate(username = name, password = password)

                if us is not None:
                    login(request, us)
                    messages.success(request, f'Welcome to InvestorHub {name}') 

                else:
                    messages.danger(request, f'Login Failed')
            
            return redirect('Index')

        else:
            return HttpResponse("404 Error no resource found")


# Handles Login 
def handleLogin(request):
        
        if request.method == 'POST':
            
            mail = request.POST['loginEmail']
            passw = request.POST['loginPassword']
            check = User.objects.filter(email = mail).exists()

            if(check):

                name = User.objects.get(email=mail).username
                us = authenticate(username = name, password = passw)

                if us is not None:
                    login(request, us)
                    messages.success(request, "Login Sucessful")
                    return redirect("Index")

                else:
                    messages.warning(request, "Please enter valid credentials")
                    return redirect ("Index")


            else:
                messages.warning(request, "Please enter valid credentials")
                return redirect ("Index")


        else:
            return HttpResponse("Error 404")


# Logout
def handleLogout(request):
    logout(request)
    messages.success(request, "Sucessfully logged out")
    return redirect("Index")