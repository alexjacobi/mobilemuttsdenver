from django.conf.urls import url

from .views import HomeView, SignUpView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
]