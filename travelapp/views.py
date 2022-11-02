from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import blog

# Create your views here.

def add(request):
    ob=blog.objects.all()
    return render(request,"index.html",{'shows':ob})





def fun(request):
    # return HttpResponse("hello world")
    # return render(request,"home.html",{'name':'adding'})
    ob = blog.objects.all()
    obj=place.objects.all()


    return render(request,"index.html",{'results':obj,'shows':ob})



# def addition(request):
#     num1=int(request.GET["num1"])
#     num2=int(request.GET["num2"])
#     num1 = int(request.POST["num1"])
#     num2 = int(request.POST["num2"])
#     num3=num1+num2
#     return render(request,"result.html",{'sum':num3})

#
# def add(request):
#     ob=blog.objects.all
#
#     return render(request,"index.html",{'shows':ob})

