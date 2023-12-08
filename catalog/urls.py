from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsCreateView, BlogListView, CreateNote, \
    BlogDetailView, UpdateNote, DeleteNote

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/create/', CreateNote.as_view(), name='create'),
    path('blog/detail/<slug:slug>', BlogDetailView.as_view(), name='detail'),
    path('blog/update/<int:pk>', UpdateNote.as_view(), name='update'),
    path('blog/delete/<int:pk>', DeleteNote.as_view(), name='delete'),
]
