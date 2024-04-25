from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product, Version
from django.views.generic import ListView, DeleteView, DetailView, TemplateView, CreateView, UpdateView


class HomePageView(TemplateView):
    template_name = "catalog/home.html"


class ContactsPageView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormSet = inlineformset_factory(Product, Version, ProductForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormSet(instance=self.object)

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

            return super().form_valid(form)

        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))



class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')
