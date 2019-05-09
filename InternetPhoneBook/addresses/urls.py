from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddressesList.as_view(), name='address_list'),
    path('address/', views.AddressesList.as_view(), name='address_list'),
    path('address/<int:pk>', views.AddressesDetails.as_view(), name='address_details'),
    path('edit/<int:pk>', views.book_update, name='address_edit'),
    path('delete/<int:pk>', views.AddressesDelete.as_view(), name='address_delete'),
    path('add/', views.address_create, name='address_new')
]