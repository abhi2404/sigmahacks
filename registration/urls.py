from django.urls import path, include

from .views import signup,login,shop_signup,shop_login,update_user,update_shopkeeper
from registration import views
urlpatterns = [
    path('' ,views.signup , name="register"),
    path('login/' ,views.login, name="login" ),
    path('shop/' , views.shop_signup ,name="shopkeepersignup"),
    path('slogin/', views.shop_login , name="shopkeeperlogin"),
    path('update/', views.update_user, name="shopkeeperlogin"),
    path('update_shopkeeper/', views.update_shopkeeper, name="shopkeeperlogin")

]