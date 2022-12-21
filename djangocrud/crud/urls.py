#crud/urls.py
from . import views
from django.urls import path
"""from django.conf import settings 
from django.conf.urls.static import static 
"""
urlpatterns = [
    #path ('admin/', admin.site.urls), 
    path ('emp', views.emp, name = 'emp'),
    path ('', views.show, name  = 'utilisateurs'),
    path ('edit/<int:id>',views.edit, name = 'edit' ), 
    path ('update/<int:id>',views.update, name = 'update'), 
    path ('delete/<int:id>',views.destroy, name = 'delete' ), 
]

# 
"""if settings.DEBUG: 
        urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
        urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)"""