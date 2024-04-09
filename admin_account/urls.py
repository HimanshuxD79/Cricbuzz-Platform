from django.urls import path
from .views import SignUp, Login

urlpatterns = [
    path('admin/signup/', SignUp.as_view()),
    path('admin/login/', Login.as_view()),
]