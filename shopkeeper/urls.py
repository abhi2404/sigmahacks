from django.urls import path, re_path
from shopkeeper import views
from .views import list_customer,finish

urlpatterns = [
     path('list/',views.list_customer,name="list"),
     path('status/',views.finish,name="finish"),
    ]