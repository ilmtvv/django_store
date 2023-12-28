

from django.forms import inlineformset_factory
from django.http import request
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, Version
from catalog.models import Product, Contacts, BlogNotes, VersionProduct


class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        #queryset = queryset.filter(owner=self.request.user)
        versions = VersionProduct.objects.filter(is_active=True,)
        for version in versions:
            version.product_pk.version = version.name
            version.product_pk.save()
        return queryset




class ContactsCreateView(CreateView):
    model = Contacts
    fields = ('name', 'message', 'phone')
    success_url = reverse_lazy('catalog:blog')


class ProductDetailView(DetailView):

    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    #fields = '__all__'
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        'title': 'обновить',
        'update': 'обновление продукта',
    }
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, VersionProduct, form=Version, extra=1)
        if self.request.method == 'POST':

            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)

        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

class ProductCreateView(CreateView):
    model = Product
    #fields = '__all__'
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        'title': 'создание',
        'update': 'sozdat product',
    }
    form_class = ProductForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


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
    #success_url = reverse_lazy('catalog:blog')
    extra_context = {
        'title': 'обновить'
    }

    def get_success_url(self):
        return reverse('catalog:detail', args=[self.kwargs.get('slug')])


class DeleteNote(DeleteView):
    model = BlogNotes
    success_url = reverse_lazy('catalog:blog')


