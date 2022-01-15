from . import views
from django.urls import path

urlpatterns = [
    path(' ', views.TableList.as_view(), name='home')
]