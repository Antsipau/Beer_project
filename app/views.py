from app.models import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout

def index(request):
    x = ""
    beer = Beer.objects.all()
    for i in beer:
        x = x + i.Manufacturer + " " + str(i.Price) + "<br>"
    return HttpResponse(x)



def indexhtml(request):
    return render(request, 'index.html', {'msg':'This is home page.'})

def errorhtml(request):
    return render(request, 'error.html', {'msg':'Please Login.'})

def recipehtml(request):
    return render(request, 'recipe.html', {'msg':'Here you can find recipes'})

def login_user(request):
    user = authenticate(
        username=request.POST["your_name"],
        password=request.POST["your_password"]
    )
    if user is None:
        return render(request,'error.html', {})
    else:
       login(request, user)
       return HttpResponseRedirect("page")

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("page")
    else:
        return HttpResponse("You are not login")

def new_register(request):
    if request.POST['password'] == "":
        return HttpResponse("пароль не может быть пустым")
    user = User.objects.create_user(
        request.POST['login'],
        password=request.POST['password'],

        # first_name='aaa',
        # last_name='bbb',
        # email='a@b.c'
    )
    # client = Client(user=user, adress='Minsk')
    # client.save()
    return HttpResponse("Everything is okay")

def show_form(request):
    return render(request, 'registration_form.html')

def privet(request):
    return render(request, 'gallary.html')

def ajax_path(request):
    response = {
        'message': request.POST["a"] + " we show you our history"
    }
    return JsonResponse(response)

def ajax_path2(request):
    users = User.objects.filter(username=request.POST['login'])
    if len(users) != 0:
        response = {"exist":1
    }
    else:
        response = {"exist":0
    }
    return JsonResponse(response)