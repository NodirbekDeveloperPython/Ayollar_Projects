from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('k_boblar/', K_BoblarViewSet.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
