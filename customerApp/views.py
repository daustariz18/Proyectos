from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = hero.objects.all().order_by('name')
    serializer_class = HeroSerializer