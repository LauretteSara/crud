#crud/urls.py
from . import views
from django.urls import path

urlpatterns = [
    #path ('admin/', admin.site.urls), 
    path ('emp', views.emp),
    path ('utilisateurs', views.show),
    path ('edit/<int:id>',views.edit ), 
    path ('update/<int:id>',views.update ), 
    path ('delete/<int:id>',views.destroy ), 
]
