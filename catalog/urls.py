from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsCreateView, BlogListView, CreateNote, \
    BlogDetailView, UpdateNote, DeleteNote, ProductUpdateView, ProductCreateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('product/<int:pk>/update_product/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>/delete_product/', ProductDeleteView.as_view(), name='delete_product'),
    path('product/create_product/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/create/', CreateNote.as_view(), name='create'),
    path('blog/detail/<slug:slug>', BlogDetailView.as_view(), name='detail'),
    path('blog/update/<slug:slug>', UpdateNote.as_view(), name='update'),
    path('blog/delete/<int:pk>', DeleteNote.as_view(), name='delete'),
]
