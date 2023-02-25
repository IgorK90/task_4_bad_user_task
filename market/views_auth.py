from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from market.models import BadUser


def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Проверяем, есть ли такой bad user
        bad_user = BadUser.objects.filter(username=username, password=password).first()
        if bad_user is None:
            return render(request, "login.html", context={"message": "Wrong username or password"})

        # Если есть, то записываем в Cookie номер пользователя (id)
        request.session["user_id"] = bad_user.id
        return HttpResponseRedirect("/")

    return render(request, "login.html")


def logout(request: HttpRequest) -> HttpResponse:
    # Чистим Cookie
    request.session["user_id"] = None
    return HttpResponseRedirect("/")
