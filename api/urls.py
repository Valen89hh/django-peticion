from django.urls import path
from .views import CompanyView, index
urlpatterns = [
    path('api/companies/', CompanyView.as_view(), name="companies_list"),
    path('api/companies/<int:id>', CompanyView.as_view(), name="companies_process"),
    path('',index, name="index")
]
