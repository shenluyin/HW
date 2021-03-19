from django.contrib import admin
from django.urls import path,include
from users.views import UsernameCountView
from users.views import register
urlpatterns = [
    path("usernames/<username:username>/", UsernameCountView.as_view()),
    path('', register)

]
