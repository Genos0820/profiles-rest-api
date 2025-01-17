from django.urls import path # type: ignore
from . import views

urlpatterns=[
    path("hello-view/",views.HelloAPIView.as_view()),
]