from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from rest_framework import routers
from stocks import views

router = routers.DefaultRouter()
router.register(r'stocks', views.StocksView, 'stock')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # re_path('.*', TemplateView.as_view(template_name='index.html')),
]
