from django.urls import path
from main_app.api.views import (KeywordListCreateAPIView, 
                                KeywordDetailAPIView, 
                                VideoListAPIView)

urlpatterns = [
    path('words/', KeywordListCreateAPIView.as_view(), name="keyword-list"),
    path('words/<int:pk>', KeywordDetailAPIView.as_view(), name="keyword-detail"),
    path('words/<int:word_pk>/video', VideoListAPIView.as_view(), name='keyword-videos')
]
