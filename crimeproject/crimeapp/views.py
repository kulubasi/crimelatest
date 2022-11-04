import re
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.template import loader
from .forms import *
from .models import *

# Create your views here.


def landingview(request):
    # messages.success(request,"Successfully logged out. Please re-login")
    return render(request,'landing.html')

def reportedcasesview(request):
    stud = Reported.objects.filter(Status__exact ='')
    return render(request,'reported.html', {'cases': stud})

def courtreportedcasesview(request):
    stud = Reported.objects.exclude(Status__exact ='')

    return render(request,'courtreported.html', {'cases': stud})

def officercrimeview(request):
    if request.method == 'POST':
        form = casesform(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('officer')
    else:
        form = casesform()
        
    
    return render(request,'report.html', {'form': form})

def individualreportview(request):
    if request.method == 'POST':
        form = individualcasesform(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('landing')
    else:
        form = individualcasesform()
        
    
    return render(request,'individualreport.html', {'form': form})

def courtcrimeview(request):
    if request.method == 'POST':
        form = casesform(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('court')
    else:
        form = casesform()
        
    
    return render(request,'report.html', {'form': form})

def homeview(request):
    return render(request,'index.html')

def signinview(request):
    form=LoginForm(request.POST or None)
    msg='no'
    # username=None
    if request.method== "POST":
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password )

            if user is not None and user.is_police_officer:
                login(request,user)
                return redirect('officer')

            if user is not None and user.is_court_Officer:
                login(request,user)
                return redirect('court')

            if user is not None and user.is_admin:
                login(request,user)
                return redirect('subadmin')

            else:
                msg="Invalid Credentials"
        else:
            msg="Error validating form"

    return render(request,'signin.html', {'form':form,'msg':msg})

def signoutview(request):
    #signout doesnt require a template
    logout(request)
    messages.success(request,"You are Logged out successfully")
    return redirect('landing')

def signupview(request):
    msg=None
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            admin=form.cleaned_data.get('is_admin')
            police=form.cleaned_data.get('is_police_officer')
            court=form.cleaned_data.get('is_court_Officer')
            # if admin == True or police == True or court == True:
            #     user=form.save()
            #     msg="User Created successfully"
            #     return redirect('subadmin')
            if admin == True and police == True and court == True:
                msg="A person can only be assigned one role"
            if admin == False and police == False and court == False:
                msg="Please Specify a persons role"
            elif  admin == True and police == True:
                msg="A person can only be assigned one role"
            elif admin == True and court == True:
                msg="A person can only be assigned one role"
            elif  court == True and police == True:
                msg="A person can only be assigned one role"
            else:
                user=form.save()
                msg="User Created successfully"
                return redirect('signupsuccess')


        else:
            msg="Form is not valid" 
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form, 'msg':msg})

def signupsuccess(request):
    return render(request,'success.html')

def officerview(request):
    off=User.objects.all
    mycases=Reported.objects.all
    return render(request,'officer.html',{'off':off,'mycases':mycases})

# def forwardview(request):
#     stud = Reported.objects.all()
#     return render(request,'forward.html',{'cases':stud})

def enrolledofficers(request):
    en=officers.objects.all
    return render(request,'court.html',{'en':en})

def registeredusersview(request):
    us=User.objects.all
    return render(request,'registeredusers.html',{'us':us})

def courtview(request):
    return render(request,'court.html')

def followupview(request):
    # model = Reported
    # template_name = "followup.html"
    # r=Reported.objects.filter(Reported(name__icontains="Boston")  )
    # return render(request,'followup.html')

    if request.method == "POST":
        form=searchForm(request.POST)
        x=request.POST.get('mysearch')
        if form.is_valid():
            x=request.POST.get('mysearch')
            
        else:
            msg="Form is not valid" 
    else:
        form=SignupForm()
    return render(request,'followup.html',{'form':form,})

def subadminview(request):
    return render(request,'subadmin.html')



        # username= request.POST.get('username')
        # username= request.POST['uname']
        # firstname= request.POST['fname']
        # lastname= request.POST['lname']
        # email= request.POST['email']
        # pswd= request.POST['pswd']
        # cpswd= request.POST['cpswd']

        # myuser=User.objects.create_user(username,email,pswd)
        # myuser.firstname=firstname
        # myuser.lastname=lastname
        # myuser.save()
        
        # messages.success(request,"Your account has been successfulyy created")
        # return redirect('signin')
    # return render(request,'signup.html')

def ready2forwardview(request):
  # mycases = Reported.objects.all()
  mycases = Reported.objects.filter(Status__exact ='')
  # template = loader.get_template('update.html')
  context = {
    'mycases': mycases,
  }
  return render(request,'ready2forward.html',context)


def forwardedview(request):
    stud = Reported.objects.exclude(Status__exact ='')

    return render(request,'forwarded.html', {'cases': stud})

def forwardview(request, id):
  mycases = Reported.objects.get(id=id)
  # template = loader.get_template('update.html')
  context = {
    'mycases': mycases,
  }
  return render(request,'forward.html',context)

def forward2courtview(request, id):
    # courtcase = Forwarded2Court()
    newStatus=request.POST.get('newStatus')
    courtcase = Reported.objects.get(id=id)
    # courtcase.Reference_Number = request.POST.get('newrefno')
    # courtcase.title = request.POST.get('newtitle')
    # courtcase.description = request.POST.get('newdescription')
    # courtcase.personreported = request.POST.get('newpersonreported')
    # courtcase.tribe = request.POST.get('newtribe')
    # courtcase.Telephone_Number = request.POST.get('newtno')
    # courtcase.Residence = request.POST.get('newResidence')
    # courtcase.Officerincharge=request.POST.get('newOfficerincharge')
    courtcase.Status=newStatus
    # courtcase.CrimeScene=request.POST.get('newCrimeScene')
    courtcase.save()


    return HttpResponseRedirect(reverse('officer'))


def updateview(request, id):
  mycases = Reported.objects.get(id=id)
  # template = loader.get_template('update.html')
  context = {
    'mycases': mycases,
  }
  return render(request,'update.html',context)

def assignoffview(request, id):
  mycases = Reported.objects.get(id=id)
  # template = loader.get_template('update.html')
  context = {
    'mycases': mycases,
  }
  return render(request,'assignoff.html',context)


def addpenaltyview(request, id):
  mycases = Reported.objects.get(id=id)
  # template = loader.get_template('update.html')
  context = {
    'mycases': mycases,
  }
  return render(request,'addpenalty.html',context)


def updatestatusview(request, id):
  # newtitle = request.POST.get('newtitle')
  # newdescription = request.POST.get('newdescription')
  # newpersonreported = request.POST.get('newpersonreported')
  # newtribe = request.POST.get('newtribe')
  # newResidence = request.POST.get('newResidence')
  # newOfficerincharge=request.POST.get('newOfficerincharge')
  newStatus=request.POST.get('newStatus')
  # newCrimeScene=request.POST.get('newCrimeScene')

  
  mycases = Reported.objects.get(id=id)
  # mycases.title = newtitle
  # mycases.description = newdescription
  # mycases.personreported = newpersonreported
  # mycases.tribe = newtribe
  # mycases.Residence = newResidence
  # mycases.Officerincharge = newOfficerincharge
  mycases.CourtStatus = mycases.CourtStatus +", "+ str(newStatus)
  # mycases.CrimeScene = newCrimeScene
  mycases.save()
  return HttpResponseRedirect(reverse('court'))


def assignoffstatusview(request, id):
  # newtitle = request.POST.get('newtitle')
  # newdescription = request.POST.get('newdescription')
  # newpersonreported = request.POST.get('newpersonreported')
  # newtribe = request.POST.get('newtribe')
  # newResidence = request.POST.get('newResidence')
  newOfficerincharge=request.POST.get('newOfficerincharge')
  # newStatus=request.POST.get('newStatus')
  # newCrimeScene=request.POST.get('newCrimeScene')

  
  mycases = Reported.objects.get(id=id)
  # mycases.title = newtitle
  # mycases.description = newdescription
  # mycases.personreported = newpersonreported
  # mycases.tribe = newtribe
  # mycases.Residence = newResidence
  mycases.Officerincharge = mycases.Officerincharge +", "+str(newOfficerincharge)
  # mycases.Status = mycases.Status +", "+ str(newStatus)
  # mycases.CrimeScene = newCrimeScene
  mycases.save()
  return HttpResponseRedirect(reverse('officer'))


def addpenaltystatusview(request, id):
  # newtitle = request.POST.get('newtitle')
  # newdescription = request.POST.get('newdescription')
  # newpersonreported = request.POST.get('newpersonreported')
  # newtribe = request.POST.get('newtribe')
  # newResidence = request.POST.get('newResidence')
  # newOfficerincharge=request.POST.get('newOfficerincharge')
  newPenalty=request.POST.get('newPenalty')
  # newCrimeScene=request.POST.get('newCrimeScene')

  
  mycases = Reported.objects.get(id=id)
  # mycases.title = newtitle
  # mycases.description = newdescription
  # mycases.personreported = newpersonreported
  # mycases.tribe = newtribe
  # mycases.Residence = newResidence
  # mycases.Officerincharge = mycases.Officerincharge +", "+str(newOfficerincharge)
  # mycases.Status = mycases.Status +", "+ str(newStatus)
  # mycases.CrimeScene = newCrimeScene
  mycases.Penalty = newPenalty
  mycases.save()
  return HttpResponseRedirect(reverse('court'))