from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('budgets', views.BudgetViewSet)
router.register('transactions', views.TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]