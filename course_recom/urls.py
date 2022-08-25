
from django.urls import path,  include
from .views import *

urlpatterns = [
    # path(r'api/chatbot/', ChatbotApi.as_view(), name='chatbot'),
    path('library',Library.as_view(), name='library')
]
