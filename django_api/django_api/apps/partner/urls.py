from django.conf.urls import url

from .views import (
#    SimpleCountryAPIView,
    PartnerDetailsAPIView,
)


urlpatterns = [
    url(r'^partner-details/(?P<pk>\d+)/$', PartnerDetailsAPIView.as_view(), name="partner-details"),
]