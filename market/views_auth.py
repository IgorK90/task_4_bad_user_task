from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render


# from market.models import BadUser


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Проверяем, есть ли такой bad user
        # bad_user = BadUser.objects.filter(username=username, password=password).first()
        user= authenticate (username=username, password=password)
        if user is None:
            return render(request, "login.html", context={"message": "Wrong username or password"})

        # Если есть, то записываем в Cookie номер пользователя (id)
        # request.session["user_id"] = bad_user.id
        login(request, user)
        return HttpResponseRedirect("/")

    return render(request, "login.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    # Чистим Cookie
    # request.session["user_id"] = None
    logout(request)
    return HttpResponseRedirect("/")
