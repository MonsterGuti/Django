from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

import accounts
from common.mixin import CheckUserIsOwner
from pets.forms import PetForm
from pets.models import Pet


class PetCreateView(CreateView):
    template_name = 'pets/pet-add-page.html'
    model = Pet
    form_class = PetForm

    def get_success_url(self):
        return reverse('accounts:details', kwargs={'pk': self.object.user.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



from django.db.models import Prefetch
from photos.models import Photo


class PetDetailView(DetailView):
    template_name = 'pets/pet-details-page.html'
    queryset = Pet.objects.prefetch_related(
        Prefetch(
            'photos',
            queryset=Photo.objects.prefetch_related('tagged_pets'),
        )
    )
    slug_url_kwarg = 'pet_slug'


class PetEditView(UpdateView, UpdateView, CheckUserIsOwner):
    template_name = 'pets/pet-edit-page.html'
    model = Pet
    form_class = PetForm
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse('pets:details',
                       kwargs={
                           'username': 'username', 'pet_slug': self.object.slug
                       })


class PetDeleteView(DeleteView):
    template_name = 'pets/pet-delete-page.html'
    model = Pet

    def get_success_url(self):
        return reverse('accounts:details', kwargs={'pk': self.object.user.pk})

    slug_field = 'slug'
    slug_url_kwarg = 'pet_slug'

    def get_initial(self):
        return self.object.__dict__
