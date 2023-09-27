from django.urls import path 
from . import views 
 
urlpatterns = [
    path('', views.product_List_create_view),
    path('<int:pk>/', views.product_deatail_view),
    path('<int:pk>/update', views.product_Update_view),
    path('<int:pk>/delete', views.product_delete_view),

]