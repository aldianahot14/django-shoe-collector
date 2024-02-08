from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions # modify these imports to match
from .models import Shoe, Cleaning, ShoeAccessory
from .serializers import ShoeSerializer, CleaningSerializer, ShoeAccessorySerializer, UserSerializer
# include the following imports
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied

# Define the home view
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the shoe-collector api home route!'}
        return Response(content)

# Updated CatList and CatDetail views below
class ShoeList(generics.ListCreateAPIView):
  serializer_class = ShoeSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
      # This ensures we only return cats belonging to the logged-in user
      user = self.request.user
      return Shoe.objects.filter(user=user)

  def perform_create(self, serializer):
      # This associates the newly created cat with the logged-in user
      serializer.save(user=self.request.user)

class ShoeDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ShoeSerializer
  lookup_field = 'id'

  def get_queryset(self):
    user = self.request.user
    return Shoe.objects.filter(user=user)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    accessories_not_associated = ShoeAccessory.objects.exclude(id__in=instance.accessories.all())
    accessories_serializer = Accessories_Serializer(accessories_not_associated, many=True)

    return Response({
        'shoe': serializer.data,
        'accessories_not_associated': accessories_serializer.data
    })

  def perform_update(self, serializer):
    shoe = self.get_object()
    if shoe.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to edit this shoe."})
    serializer.save()

  def perform_destroy(self, instance):
    if instance.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to delete this shoe."})
    instance.delete()

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

# include the registration, login, and verification views below
# User Registration
class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

# User Login
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })