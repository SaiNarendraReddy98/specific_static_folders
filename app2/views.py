from django.shortcuts import render

# Create your views here.
def application(request):

    return render(request,'application.html')

def successful(request):
    d={'name':'Kagithala Narendra Sai '}

    return render(request,'successful.html',d)