from django.urls import path
from .views import LikeListView, LikeDetailView

urlpatterns = [
  path('', LikeListView.as_view()),
  path('<int:pk>/', LikeDetailView.as_view()),
]