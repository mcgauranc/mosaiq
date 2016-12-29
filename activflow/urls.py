"""URL configuration for django app"""

from django.conf.urls import include, url
from django.contrib import admin

import report_builder.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^report_builder/', include(report_builder.urls)),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'', include('activflow.core.urls')),

]
