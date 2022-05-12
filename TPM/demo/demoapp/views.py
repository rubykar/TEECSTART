from django.shortcuts import render
from demoapp.forms import Organisation_form,Admin_form,Manager_form,Client_form,Employee_form,Task_form, Work_form,Department_form,UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView
from demoapp.models import Organisation,Admin,Manager,Department,Employee,Task,Client,Work,UserProfileInfo
from django.core import serializers
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render (request,'demoapp/index.html')


def profile(request):
    return render(request,'demoapp/profile.html')

@login_required
def special(request):
    return HttpResponse('You are logged in nice!')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('demoapp:dash'))


def dash(request):
    return render(request,'demoapp/Dashboard.html')


def dash2(request):
    return render(request,'demoapp/Dashboard2.html')



def dash3(request):
    return render(request,'demoapp/dashboard_dept.html')

def dash4(request):
    return render(request,'demoapp/dashboard_task.html')

def dash5(request):
    return render(request,'demoapp/dashboard_work.html')

def dep_form(request):
    form = Department_form()


    if request.method =='POST':
        form = Department_form(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return index(request)


        else:
            print("ERROR!")   


    return render(request,'demoapp/dept.html',{'form':form}) 





def admin_form(request):
    form = Admin_form()


    if request.method =='POST':
        form = Admin_form(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return index(request)


        else:
            print("ERROR!")   


    return render(request,'demoapp/login.html',{'form':form}) 
            


def mang_form(request):
    form = Manager_form()


    if request.method =='POST':
        form = Manager_form(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return index(request)


        else:
            print("ERROR!")   


    return render(request,'demoapp/login.html',{'form':form}) 




def client_form(request):
    form = Client_form()


    if request.method =='POST':
        form = Client_form(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('demoapp:dash2'))


        else:
            print("ERROR!")   


    return render(request,'demoapp/form_page.html',{'form':form}) 




def org_form(request):
    form = Organisation_form()


    if request.method =='POST':
        form = Organisation_form(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return index(request)


        else:
            print("ERROR!")   


    return render(request,'demoapp/login.html',{'form':form}) 




def emp_form(request):
    form = Employee_form()


    if request.method =='POST':
        form =Employee_form(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return index(request)


        else:
            print("ERROR!")   


    return render(request,'demoapp/login.html',{'form':form}) 




def work_form(request):
    form = Work_form()


    if request.method =='POST':
        form =Work_form(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return index(request)


        else:
            print("ERROR!")   


    return render(request,'demoapp/login.html',{'form':form}) 





def task_form(request):
    form = Task_form()


    if request.method =='POST':
        form =Task_form(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return index(request)


        else:
            print("ERROR!")   


    return render(request,'demoapp/task.html',{'form':form}) 




def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        



        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()



            profile = profile_form.save(commit = False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            

            registered = True


        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'demoapp/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



def user_login(request):



    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')



        user = authenticate(username=username,password=password)


        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('demoapp:dash'))


            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")


        else:
            print("Someone tried to login and Failed!")
            print("Username: {} and password {}".format(username,password) ) 
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request,'demoapp/login.html',{})    



def client_detail_view(request):
    clients = Client.objects.all()
    return render(request,'demoapp/Dashboard2.html', {'clients': clients})

def client_profile_view(request,pk):
    client=Client.objects.get(id=pk)
    return render(request,'demoapp/profile.html',{'client':client})


def updateOrder(request,pk):
    i = Client.objects.get(id=pk)
    form = Client_form(instance=i)

    if request.method =='POST':
        form = Client_form(request.POST,instance=i)


        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('demoapp:dash2'))


        else:
            print("ERROR!")

    context={"form":form}
    return render(request,'demoapp/form_page.html',context)


def deleteClient(request,pk):
   i=Client.objects.get(id=pk)
   if request.method=="POST":
          i.delete() 
          return HttpResponseRedirect(reverse("demoapp:dash2")) 
   context = {'client':i}
   return render(request,'demoapp/delete.html',context)