from django.urls import path, include # type: ignore
from . import views
from rest_framework.routers import DefaultRouter # type: ignore

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSets, base_name='hello-viewset')

urlpatterns=[
    path("hello-view/",views.HelloAPIView.as_view()),
    path("",include(router.urls)),
]