from django.shortcuts import render
from django.http import HttpResponse
from forms_app import forms
# Create your views here.
def index(request):
    index_dict={}
    return render(request,'forms_app/django_forms.html',context=None)
def form_view(request):
    form=forms.FormName()# we got our form which have features included in FormName class in forms.py
    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("VALIDATION SUCESSFULL!!")
            print('NAME: '+form.cleaned_data['name'])
            print('Email: '+form.cleaned_data['email'])
            print('Text: '+form.cleaned_data['text'])
    #form=forms.FormName()
    return render(request,'forms_app/formpage.html',{'form':form})
