from django.contrib import admin
from django.urls import path, include

from mysite.core import views


#from mysite.core.views import  vc_portal, vc_learn, st_hub,st_connect, careers, library, contacts_connect, register, login

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
	
	
#	path('contacts/', views.contacts_connect, name='contacts'),
	path('vcportal/', views.vc_portal, name='vcportal'),
	path('vclearn/', views.vc_learn, name='vclearn'),
	path('studenthub/', views.st_hub, name='studenthub'),
	path('studentconnect/', views.st_connect, name='studentconnect'),
	path('careers/', views.careers, name='careers'),
	path('library/', views.library, name='library'),
]
