from django.shortcuts import render

# Create your views here.

def rendaringdata(request):
    payload={
        'movie':'RRR',
        'cast':'rambhem',
        'award':'goldenaward'
    }
    context={'data':payload}
    return render(request,'home.html',context)
