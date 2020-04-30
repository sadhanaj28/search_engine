from django.urls import path

from .views import SearchEXP


urlpatterns = [
    path('api/v1/summaries_list/', SearchEXP.as_view()),
]

