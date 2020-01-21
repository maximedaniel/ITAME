from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.classification, name='Classification'),
    #url(r'chronology/$', views.chronology, name='Chronology'),
    #url(r'vision/$', views.vision, name='Vision'),
    #url(r'hypothesis/$', views.hypothesis, name='Hypothesis'),
    url(r'^(?P<interactive_system_id>.*)/$', views.interactive_system, name='interactive_system'),
]