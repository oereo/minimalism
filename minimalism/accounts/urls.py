from django.urls import path
from accounts.views import login, create_user, signup, signup_user

urlpatterns = [
    path('login/', login, name="login"),
    path('login-user', create_user, name='create_user'),
    path('signup/', signup, name="signup"),
    path('signup-user', signup_user, name="signup_user")
]
