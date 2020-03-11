from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('Songs', views.ListSongsView)

urlpatterns = [
    path('', include(router.urls))
    #path('', ListSongsView.as_view(), name="songs-all"),
]
