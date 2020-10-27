from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'basic_app/homepage.html')


def other(request):
    return render(request,'basic_app/otherpage.html')


def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
