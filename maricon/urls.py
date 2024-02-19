from django.urls import path

from .views import IndexView, CommitteeView, RegisterView, OtpView, SubmissionView, LoginView

urlpatterns = [
    path('', IndexView.as_view(), name='maricon'),
    path('committee/', CommitteeView.as_view(), name='committee'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/otp/', OtpView.as_view(), name='otp'),
    path('login/otp/', OtpView.as_view(), name='otp'),
    path('submission/', SubmissionView.as_view(), name='submission'),
    path('login/', LoginView.as_view(), name='login'),


]
