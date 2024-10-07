from django.urls import path

from ap1.views import viewshtml

urlpatterns = [
    path("strona/", viewshtml),
    path("strona/<int:id>", viewshtml)
]