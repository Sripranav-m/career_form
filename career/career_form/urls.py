from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

from . import views

urlpatterns = [
    path('',views.career_form,name='career_form'),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)