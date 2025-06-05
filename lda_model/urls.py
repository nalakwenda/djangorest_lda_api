from django.urls import path
from .views import LDATopicView

urlpatterns = [
    path('classify/', LDATopicView.as_view(), name='classify-text')
]
