from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from devup.views import UpList, UpDetail, UpCreate, UpUpdate

app_name = 'devup'

urlpatterns = [
    url(r'^up_list$', UpList.as_view(), name='up_list'),
    url(r'^up_create$', UpCreate.as_view(), name='up_create'),
    url(r'^up_detail/(?P<pk>[-\w]+)/$', UpDetail.as_view(), name='up_detail'),
    url(r'^(?P<pk>[-\w]+)/$', UpDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update$', UpUpdate.as_view(), name='update'),

]
