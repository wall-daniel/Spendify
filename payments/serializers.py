from rest_framework import serializers
from payments.models import Payment


class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = ['id', 'description', 'pub_date', 'amount']

