from awardapp import views
from django.urls import path
from .views import *


urlpatterns=[
    path('profile/',profile_list,name='profile'),
    path('profile/<int:id>',profile_detail),
    path('display_profile/',display_profile,name='profileform'),
    path('',views.index, name='home'),
    path('register/',register_user,name='register'),
    path('display_project/',display_project),
    path('votes/',dis_votes,name='votes'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.login_user,name='logout'),
    path('search/',views.search,name='search'),
    path('project/',project_list,name="project"),
    path('display_project/',display_project,name='projectform'),
    path('output/',views.output,name='output'),
]