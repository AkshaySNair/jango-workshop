from django.conf.urls import url
from . import views
urlpatterns=[
	url('',views.HomePageView.as_view(),name='home')
	]