from django.urls import path 
from . import views 
 
urlpatterns = [
    path('', views.product_mixin_views),
    path('<int:pk>/', views.product_mixin_views),
    path('<int:pk>/update', views.product_mixin_views),
    path('<int:pk>/delete', views.product_mixin_views),

]