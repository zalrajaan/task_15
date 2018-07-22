from rest_framework.generics import ListAPIView,RetrieveAPIView ,DestroyAPIView, RetrieveUpdateAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer,Anything2, Anything3, Anything4

class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer

# Complete me
class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = Anything2
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'

# Complete me
class RestaurantUpdateView(RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = Anything3
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'


# Complete me
class RestaurantDeleteView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = Anything4
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'

