from django.contrib import admin
from django.urls import path

from app_1.views import ReviewFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', ReviewFormView.as_view(), name='reviews')
]
