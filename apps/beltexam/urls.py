from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$',views.user_registration),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^add$', views.add),
    url(r'^wish_items/(?P<id>\d+)$', views.wishitems), 




    url(r'^wish_items/create$', views.additem),
    # url(r'^createitem$', views.createitem),
    url(r'^logout$', views.logout),
]



    
#     url(r'^travels/destination/(?P<id>\d+)$', views.destination), 
#     url(r'^travels/add$', views.add_travel),
#     url(r'^join/(?P<id>\d+)$', views.join),