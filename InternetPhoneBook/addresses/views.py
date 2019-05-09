from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.utils import timezone
from .models import Address


# https://rayed.com/posts/2018/05/django-crud-create-retrieve-update-delete/

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'second_name', 'phone', 'email_address']

class AddressesList(ListView):
    model = Address

class AddressesDetails(DetailView):
    model = Address


def book_update(request, pk, template_name='addresses/address_form.html'):
    address= get_object_or_404(Address, pk=pk)
    address.updated = timezone.now()
    form = AddressForm(request.POST or None, instance=address)
    if form.is_valid():
        form.save()
        return redirect('address_list')
    return render(request, template_name, {'form':form})

class AddressesDelete(DeleteView):
    model = Address
    success_url = reverse_lazy('address_list')

def address_create(request, template_name='addresses/address_form.html'):
    form = AddressForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('address_list')
    return render(request, template_name, {'form':form})