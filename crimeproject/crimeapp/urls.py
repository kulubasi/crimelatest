"""crimeapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from crimeapp.views import *


urlpatterns = [
    path('crime',officercrimeview, name="regcrime"),
    path('crime',courtcrimeview, name="courtcrime"),
    path('crimehome',homeview, name="crimehome"),
    path('signup',signupview, name="signup"),
    path('signin',signinview, name="signin"),
    path('signout',signoutview, name="signout"),
    path('officer',officerview, name="officer"),
    path('ready2forward',ready2forwardview, name="ready2forward"),
    path('forwarded',forwardedview, name="forwarded"),
    path('court',courtview, name="court"),
    path('subadmin',subadminview, name="subadmin"),
    path('followup',followupview, name="followup"),
    path('subdmin/signupsuccess',signupsuccess, name="signupsuccess"),
    path('',landingview, name="landing"),
    path('reported',reportedcasesview, name="reported"),
    path('courtreported',courtreportedcasesview, name="courtreported"),
    path('registeredusers',registeredusersview, name="registeredusers"),
    path('individualreport',individualreportview, name="individualreport"),
    path('update/<int:id>',updateview, name="update"),
    path('update/updatestatus/<int:id>', updatestatusview, name='updatestatus'),
    path('assignoff/<int:id>',assignoffview, name="assignoff"),
    path('assignoff/assignoffstatus/<int:id>', assignoffstatusview, name='assignoffstatus'),
    path('addpenalty/<int:id>',addpenaltyview, name="addpenalty"),
    path('addpenalty/addpenaltystatus/<int:id>', addpenaltystatusview, name='addpenaltystatus'),
    path('forward/<int:id>',forwardview, name="forward"),
    path('forward/forward2court/<int:id>', forward2courtview, name='forward2court'),]
