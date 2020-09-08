from django.urls import path, include

from apps.covidtracker import views
urlpatterns = [
    path('', views.home, name="home"),
    path('countrystat', views.searchcountry, name="searchcountry"),
    path('caseoverview', views.overview, name="overview"),
]
