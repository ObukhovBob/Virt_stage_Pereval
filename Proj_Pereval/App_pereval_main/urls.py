from django.urls import path
from .views import SubmitData

urlpatterns = [
    path('api/v1/submitData/', SubmitData.as_view(), name='submitData'),
    path('api/v1/submitData/<int:pk>/', SubmitData.as_view(), name='submitData'),
    path('api/v1/submitData/?user__email=email/', SubmitData.as_view(), name='email'),
]
