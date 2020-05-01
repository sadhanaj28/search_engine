from django.urls import path

from .views import SummarySearchView


urlpatterns = [
    path('api/v1/summaries_list/', SummarySearchView.as_view(), name='summaries-list'),
]

