from django.urls import path
from .views import WorkImagesByCategory
from .views import submit_order

urlpatterns = [
    path('images/<str:category>/', WorkImagesByCategory.as_view(), name='category-images'),
     path('submit-order/', submit_order, name='submit_order'),
]
