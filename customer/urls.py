from django.urls import path, re_path
from customer import views
from .views import shop_category

urlpatterns = [
     path('category/',views.shop_category,name="category"),
     path('location/',views.location,name="location"),
    ]