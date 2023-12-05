from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product, Contacts


class ProductListView(ListView):
    model = Product


class ContactsCreateView(CreateView):
    model = Contacts
    fields = ('name', 'message', 'phone')
    success_url = reverse_lazy('catalog:contacts')


class ProductDetailView(DetailView):

    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset



