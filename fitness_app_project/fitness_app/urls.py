from django.urls import path
from . import views

urlpatterns = [
  ############## LOG IN ###############
  path('', views.login, name="login"),
  path('', views.login_view, name="login"),
  path('signup/', views.signup_view, name="signup"),
  path('logout/', views.logout_view, name="logout"),
  ############# HOMEPAGE ##############
  path('homepage/', views.homepage, name="homepage"),
  ############# PROFILE ###############
  path('user/<username>/', views.dashboard, name='dashboard'),
]
