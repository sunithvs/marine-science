from django.urls import path

from .views import IndexView, CommitteeView, RegisterView

urlpatterns = [
    path('', IndexView.as_view(), name='maricon'),
    path('committee/', CommitteeView.as_view(), name='committee'),
    path('register/', RegisterView.as_view(), name='register'),

]
