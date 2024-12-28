from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from resume.forms import ResumeForm

# Resume Page View 
class Resume(View):
    def get(self,request):
        if request.user.is_authenticated:
            form = ResumeForm()
            return render(request,"resume/resume.html",{"form":form})
        else:
            return HttpResponseRedirect("/login")