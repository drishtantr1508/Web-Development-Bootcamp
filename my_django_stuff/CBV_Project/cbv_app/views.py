from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView, DetailView, CreateView,UpdateView,DeleteView
from . import models
# Create your views here.
class Homepage(TemplateView):
    #for rendering html page
    template_name='cbv_app/cbv_app_homepage.html'
#for injecting templates
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']='This is example of a basic injection'
        return context
class SchoolList(ListView):
    context_object_name='schools'
    model= models.School
    template_name="cbv_app/student_list.html"
class SchoolDetail(DetailView):#is linked by primary key only.
    context_object_name="school_detail"
    model=models.School
    template_name ="cbv_app/student_detail.html"

class SchoolCreateView(CreateView):#this creates a form automatically and saves automatically ,petty easy
    fields=('name','principal','location')
    model=models.School
class SchoolUpdateView(UpdateView):# linked by primary key only.
    fields=('principal','name')
    model=models.School
class SchoolDeleteView(DeleteView):# linked by primary key only.
    #context_object_name='del_school'
    model=models.School
    success_url=reverse_lazy('cbv_app:list')
