from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Shoe, Cleaning, ShoeAccessory
from .serializers import ShoeSerializer, CleaningSerializer, ShoeAccessorySerializer


# Define the home view
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the shoe-collector api home route!'}
        return Response(content)

class ShoeList(generics.ListCreateAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

class ShoeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    lookup_field = 'id'

class CleaningListCreate(generics.ListCreateAPIView):
    serializer_class = CleaningSerializer

def get_queryset(self):
    shoe_id = self.kwargs['shoe_id']
    return Cleaning.objects.filter(shoe_id=shoe_id)

def perform_create(self, serializer):
    shoe_id = self.kwargs['shoe_id']
    shoe = Shoe.objects.get(id=shoe_id)
    serializer.save(shoe=shoe)


class CleaningDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CleaningSerializer
    lookup_field = 'id'

    def get_queryset(self):
        clean_id = self.kwargs['clean_id']
        return Cleaning.objects.filter(clean_id=clean_id)

class ShoeAccessoryList(generics.ListCreateAPIView):
    queryset = ShoeAccessory.objects.all()
    serializer_class = ShoeAccessorySerializer

class ShoeAccessoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoeAccessory.objects.all()
    serializer_class = ShoeAccessorySerializer
    lookup_field = 'id'