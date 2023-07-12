from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView
from .forms import RegForm,Logform

from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.urls import reverse_lazy




# Create your views here.
def login(request):
    return render(request,'log.html')

def register(request):
    return render(request,'register.html')

#view for registration
class Regview(CreateView):
    template_name="register.html"
    form_class=RegForm
    success_url=reverse_lazy('logv')

#view for login
class LogView(FormView):
    template_name="log.html"
    form_class=Logform
    def post(self,request,*args,**kwargs):
        formdata=Logform(data=request.POST)
        if formdata.is_valid():
            user_name=formdata.cleaned_data.get("username")
            pswd=formdata.cleaned_data.get("password")
            user_data=authenticate(request,username=user_name,password=pswd)
            if user_data:
                return redirect("Home")
            else:
                return render(request,'log.html',{'form':formdata})
            
            
            
class Lgout(View):
    def get(self,request):
        logout(request)
        return redirect("logv")