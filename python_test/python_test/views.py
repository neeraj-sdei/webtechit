from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import FormView, UpdateView, ListView

from .models import Client, ClientForm
# Insert views here


class ClientAddView(FormView):
    # using FormView to dynamically show form in template and adding client
    template_name = "add_client.html"
    form_class = ClientForm
    model = Client

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/list')


class ClientListView(ListView):
    # listing clients using generic ListView
    model = Client
    template_name = 'list_client.html'

    def get_queryset(self):
        query = Q()
        name = self.request.GET.get('name')
        email = self.request.GET.get('email')
        phone = self.request.GET.get('phone')
        suburb = self.request.GET.get('suburb')
        sort = self.request.GET.get('sort', '-created_at')
        # create a query from all the request params
        if name:
            query |= Q(client_name__icontains=name)
        if email:
            query |= Q(email__icontains=email)
        if phone:
            query |= Q(phone_number__icontains=phone)
        if suburb:
            query |= Q(suburb__icontains=suburb)
        return Client.objects.filter(query).order_by(sort)

    # used to set the values in search form
    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        context['name'] = self.request.GET.get('name', '')
        context['email'] = self.request.GET.get('email', '')
        context['phone'] = self.request.GET.get('phone', '')
        context['suburb'] = self.request.GET.get('suburb', '')
        return context


class ClientUpdateView(UpdateView):
    # update view for client
    template_name = 'edit_client.html'
    form_class = ClientForm
    model = Client

    def get_object(self, *args, **kwargs):
        client = get_object_or_404(Client, id=self.kwargs['pk'])
        return client

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/list')
