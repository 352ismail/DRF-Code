from django.urls import path 
from . views import * 

urlpatterns = [
    path('',api_home,name="api_home"),
    # path('get_by_id/',get_by_id,name="get_by_id"),
    # path('get_with_details/',get_with_deatils,name = "get_with_details"),

]
