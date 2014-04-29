import os
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from bookmarks.views import *
from django.conf.urls import patterns, include, url
from rest_framework import routers
from bookmarks import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


site_media = os.path.join(
  os.path.dirname(__file__), 'site_media'
)

urlpatterns = patterns('',
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  
  (r'^$', main_page),
  (r'^user/(\w+)/$', user_page),
  #Session management
  (r'^login/$', 'django.contrib.auth.views.login'),
  (r'^logout/$', logout_page),
  (r'^register/$', register_page),
  (r'register/success/$', direct_to_template,
    {'template': 'registration/register_success.html'}),
  (r'^tag/([^\s]+)/$', tag_page),
  (r'^tag/$', tag_cloud_page),
  #Account management
  (r'^save/$', bookmark_save_page),
  # Site media
  (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': site_media}),
  

)
