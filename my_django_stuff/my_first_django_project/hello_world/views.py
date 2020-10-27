from django.shortcuts import render
from django.http import HttpResponse
from hello_world.models import AccessRecord,WebPage,Topic
# Create your views here.
#def index(request):
    #return HttpResponse("Hello World!")
def index2(request):
    webpage_list=AccessRecord.objects.order_by("date")
    my_dict={'insert_me':'Hello I am from views.py',
    'insert_book':'hcverma',
    'insert_img':'This is a picture of milky way!(:)',
    'access_records':webpage_list}
    return render(request,'index.html',context=my_dict)
