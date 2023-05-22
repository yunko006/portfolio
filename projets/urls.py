from django.urls import path
from .views import ProjetProList, ProjetProDetail

urlpatterns = [
    path("<int:pk>/", ProjetProDetail.as_view(), name="projetpro_detail"),
    path("", ProjetProList.as_view(), name="projetpro_list"),
]
