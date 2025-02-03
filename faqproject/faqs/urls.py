from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet
from .views import FaqSearchView
from . import views

router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename='faq')

urlpatterns = [
    path('', include(router.urls)),
   path('faqs/search/', FaqSearchView.as_view(), name='faq-search'),
]