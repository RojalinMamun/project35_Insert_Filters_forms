from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *
def Insert_details(request):
    d={'TFO':TopicForm(),'WFO':WebpageForm(),'AFO':AccessRecordForm}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        WFD=WebpageForm(request.POST)
        AFD=AccessRecordForm(request.POST)

        if TFD.is_valid() and WFD.is_valid() and AFD.is_valid():
            NTFO=TFD.save(commit=False)
            NTFO.save()

            NWFO=WFD.save(commit=False)
            NWFO.topic_name=NTFO
            NWFO.save()

            NAFO=AFD.save(commit=False)
            NAFO.name=NWFO
            NAFO.save()
        
            return HttpResponse ('Data is submitted')

        else:
            return HttpResponse('Data id not valid')

    return render(request,'Insert_details.html',d)

    




