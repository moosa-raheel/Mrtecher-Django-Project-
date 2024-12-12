from django.urls import path
from .views import home_page,SignUp,Login,logout_page
urlpatterns = [
    path("",home_page,name="home"),
    path("signup/",SignUp.as_view(),name="signup"),
    path("login/",Login.as_view(),name="login"),
    path("logout/",logout_page,name="logout")
]
