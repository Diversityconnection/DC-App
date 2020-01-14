from rest_framework import viewsets

from .serializers import CitySerializer, City


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query is None:
            return self.queryset
        
        return self.queryset.filter(title__istartswith=query)
