# coding=utf-8
from django.conf.urls import url
from patient.views import BloodgroupList, BloodgroupDetail
from patient.views import BloodgroupCreate , BloodgroupDelete ,BloodgroupUpdate
from patient.views import PatientCreate, PatientUpdate , PatientDelete

app_name = 'patient'

# release Release
urlpatterns = [
    url(r'^$', BloodgroupList.as_view(), name='bloodgroup-list'),
    url(r'^bloodgroup/(?P<pk>\d+)$', BloodgroupDetail.as_view(), name='bloodgroup-detail'),
    url(r'^bloodgroup/add/', BloodgroupCreate.as_view(), name='bloodgroup-add'),
    url(r'^bloodgroup/update/(?P<pk>\d+)$', BloodgroupUpdate.as_view(), name='bloodgroup-update'),
    url(r'^bloodgroup/delete/(?P<pk>\d+)$', BloodgroupDelete.as_view(), name='bloodgroup-delete'),
    url(r'^bloodgroup/patient/add/(?P<bloodgroupid>\d+)$', PatientCreate.as_view(), name='patient-add'),
    url(r'^bloodgroup/patient/update/(?P<pk>\d+)$', PatientUpdate.as_view(), name='patient-update'),
    url(r'^bloodgroup/patient/delete/(?P<pk>\d+)$', PatientDelete.as_view(), name='patient-delete'),
]