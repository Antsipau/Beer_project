from app.models import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext as _, activate
from django.conf import settings

def index(request):
    x = ""
    beer = Beer.objects.all()
    for i in beer:
        x = x + "This is beer from the Manufacturer: " + i.Manufacturer + ". The name of this beer is "\
            + str(i.Beer_name) + ". Our price for you is " + str(i.Price) + " rubels." + "<br>"
    return HttpResponse(x)


def indexhtml(request):
    activate('en')

    response = render(request, 'index.html', {'msg':'This is home page.',
    "photo1": Beer.objects.filter(id=1)[0],
    "photo2": Beer.objects.filter(id=2)[0],
    "photo3": Beer.objects.filter(id=3)[0],
    "photo4": Beer.objects.filter(id=4)[0],
    "photo5": Beer.objects.filter(id=5)[0],
    })
    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME, "ru",
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
    return response

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


