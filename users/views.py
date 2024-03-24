from django.shortcuts import render, redirect
import csv
# Create your views here.
# def createuser(request):
    # return render(request, 'createuser.html')
    # if request.method == 'POST':
    #     dict1 = request.POST
    #     with open('createuseraccount.csv', 'a') as csvfile:
    #         wrt = csv.writer(csvfile)
    #         for key,value in dict1.items():
    #             wrt.writerow([key, value])

    # return render(request, 'createuser.html')
    


# def createuseraccount(request):
#     if request.method == 'POST':
#         dict1 = request.POST
#         with open('createuseraccount.csv', 'a') as csvfile:
#             wrt = csv.writer(csvfile)
#             for key,value in dict1.items():
#                 wrt.writerow([key, value])

#     return render(request, 'createuser.html')


from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User,auth
from django.contrib.auth import login, authenticate
from django.contrib import messages


# def redirect_view(request):
#     response = redirect('redirect-success')
#     return response

def createuser(request):

    if request.method == 'POST':

        username1 = request.POST['username']

        email1 = request.POST['email']

        password = request.POST['password']

        password1 = request.POST['password']

        if password== password1:

            if User.objects.filter(email = email1).exists():

                messages.info(request,'Email already exists')

                return redirect('/create-user/')

            elif User.objects.filter(username = username1).exists():

                messages.info(request,'USername already exists')

                return redirect('/create-user/')

            else:

                user= User.objects.create_user(username=username1,email=email1,password=password)

                user.save()

                return redirect('/')

        else:

            messages.info(request,' Password not the same')

            return redirect('/create-user/')

    else:

        return render(request, 'createuserid.html')
    

def loginuser(request):

    if request.method == 'POST':

        username1 = request.POST['username']

        # email1 = request.POST['email']

        password1 = request.POST['password1']

        user = authenticate(username=username1, password=password1)
        if user:  # If the returned object is not None
                login(request, user)  # we connect the user
                return redirect('/')
        else:
               messages.info(request,'Usernnnname or password entered are incorrect. Please enter again')
               return redirect('/login-user/')

    


    else:

        return render(request, 'login-user.html')