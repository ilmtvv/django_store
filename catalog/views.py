from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, Contacts, BlogNotes


class ProductListView(ListView):
    model = Product


class ContactsCreateView(CreateView):
    model = Contacts
    fields = ('name', 'message', 'phone')
    success_url = reverse_lazy('catalog:contacts')


class ProductDetailView(DetailView):

    model = Product



class BlogListView(ListView):
    model = BlogNotes

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_active=True)
        return queryset

class BlogDetailView(DetailView):
    model = BlogNotes

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()

        return self.object




class CreateNote(CreateView):
    model = BlogNotes
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('catalog:blog')

    extra_context = {
        'title': 'создать'
    }


    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class UpdateNote(UpdateView):
    model = BlogNotes
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('catalog:blog')
    extra_context = {
        'title': 'обновить'
    }

    def get_success_url(self):
        return reverse('catalog:detail', args=[self.kwargs.get('pk')])


class DeleteNote(DeleteView):
    model = BlogNotes
    success_url = reverse_lazy('catalog:blog')


