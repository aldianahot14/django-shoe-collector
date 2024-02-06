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

  # add (override) the retrieve method below
def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this cat
    accessories_not_associated = ShoeAccessory.objects.exclude(id__in=instance.accessories.all())
    accessories_serializer = ShoeAccessorySerializer(accessories_not_associated, many=True)


    return Response({
        'shoe': serializer.data,
        'accessories_not_associated': accessories_serializer.data
    })


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

class AddShoeAccessoryToShoe(APIView):
  def post(self, request, shoe_id, shoeAccessory_id):
    shoe = Shoe.objects.get(id=shoe_id)
    shoeAccessory = ShoeAccessory.objects.get(id=shoeAccessory_id)
    shoe.shoeAccessory.add(shoeAccessory)
    return Response({'message': f'ShoeAccessory {shoeAccessory.name} added to Shoe {shoe.name}'})
