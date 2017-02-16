from django.conf.urls import url
from . import views

app_name = 'usermanager'

urlpatterns = [
    #url(r'^uindex/$', views.uindex, name='uindex'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login_user/$',views.login_user, name='login_user'),
    url(r'^logout_user/$',views.logout_user, name='logout_user'),
    url(r'^create_uprofile/$',views.create_uprofile, name='create_uprofile' ),
]