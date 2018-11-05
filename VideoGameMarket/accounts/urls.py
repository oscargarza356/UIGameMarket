from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signup, name = 'signup'),
    url(r'^login/', views.loginView, name = 'login'),
    url(r'^logout/', views.logoutView, name = 'logout'),
]
