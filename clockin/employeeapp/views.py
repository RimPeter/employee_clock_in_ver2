from django.shortcuts import render

def home(request):
    
    #return render(request, 'home.html')
    return HttpResponse("This is my homepage")
