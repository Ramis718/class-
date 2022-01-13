from django.contrib import admin
from django.urls import path
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/data/', views.index ),
    path('api/v1/movies/', views.movie_list_view),
    path('api/v1/movies/<int:id>/', views.movie_datail_view),

]
