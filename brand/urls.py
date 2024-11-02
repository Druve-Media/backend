from django.urls import path
from .views import GetUserBrandsView  # Adjust import based on your project structure

urlpatterns = [
    path('/getbrand', GetUserBrandsView.as_view(), name='get_user_brands'),  # New API endpoint
    # other URL patterns...
]
