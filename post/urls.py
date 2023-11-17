from django.urls import path,include
from . import views


urlpatterns = [ 
    path('post/',views.Post , name="post"),
    path('viewall/',views.ViewAll , name="viewall"),
    path('search/',views.Search , name="search"),
    
]