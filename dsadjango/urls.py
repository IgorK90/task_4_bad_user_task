from django.contrib import admin
from django.urls import path
from market.views import show_cars, audi_purchase, payment
from market.views_auth import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_cars),
    path('login', login_view),
    path('logout', logout_view),
    path('buy_car/<int:id_>', audi_purchase),
    path('payment/<int:id_>', payment),
    # добавьте два url: для login и для logout
]
