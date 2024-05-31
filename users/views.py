from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payments
from users.serialyzers import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ("course", "lesson", "method")
    ordering_fields = ("date",)
