from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from todo import models
from djangle import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'todos', models.TodoViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

    url(r'^api/', include(router.urls)),
    url(r'^_forms', views.render_serializers),

    url(r'^$', TemplateView.as_view(template_name="index.html"))
)
