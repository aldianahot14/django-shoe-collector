from django.urls import path

# import Home view from the views file
from .views import Home, ShoeList, ShoeDetail, CleaningListCreate, CleaningDetail, ShoeAccessoryList, ShoeAccessoryDetail, AddShoeAccessoryToShoe, CreateUserView, LoginView, VerifyUserView

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('shoes/', ShoeList.as_view(), name='shoe-list'),
  path('shoes/<int:id>/', ShoeDetail.as_view(), name='shoe-detail'),
  path('shoes/<int:shoe_id>/cleanings/', CleaningListCreate.as_view(), name='cleaning-list-create'),
  path('shoes/<int:shoe_id>/cleanings/', CleaningDetail.as_view(), name='cleaning-detail'),
  path('shoeaccessory/', ShoeAccessoryList.as_view(), name='shoeaccessory-list'),
  path('shoeaccessory/<int:id>/', ShoeAccessoryDetail.as_view(), name='shoeaccessory-detail'),
  path('shoes/<int:shoe_id>/add_shoeaccessory/<int:shoeAccessory_id>/', AddShoeAccessoryToShoe.as_view(), name='add-shoeaccessaory-to-shoe'),
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),
  path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
]

