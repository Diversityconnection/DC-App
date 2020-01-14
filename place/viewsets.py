from rest_framework import viewsets

from .serializers import CitySerializer, City


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
