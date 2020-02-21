from django.urls import path,include,re_path
from .import views
urlpatterns =[
    re_path(r'^location/$',views.RegionListApiView.as_view(),name="RegionListApiView"),
    re_path(r'^location/(?P<region>\w+)/$',views.CountryListApiView.as_view(),name="CountryListApiView"),
    re_path(r'^location/(?P<region>\w+)/(?P<country>\w+)/$',views.StateListApiView.as_view(),name="StateListApiView"),
    re_path(r'^location/(?P<region>\w+)/(?P<country>\w+)/(?P<state>\w+)/$',views.CityListApiView.as_view(),name="CityListApiView"),
]