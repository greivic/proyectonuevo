from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.forms import InstrumentoForm
from app.models import Instrumento

class InstrumentoListView(ListView):
    model = Instrumento
    template_name = 'list_card_instrumento.html'

    def get_context_data(self, **kwargs):
        context = super(InstrumentoListView, self).get_context_data()
        context['title'] = 'Listado de instrumentos musicales'
        context['all_instrumento'] = Instrumento.objects.all()
        return context


class InstrumentoDetailsView(DetailView):
    model = Instrumento
    template_name = 'details_instrumento.html'

    def get_context_data(self, **kwargs):
        context = super(InstrumentoDetailsView, self).get_context_data()
        context['title'] = 'Detalle'
        context['all_instrumento'] = Instrumento.objects.all()
        return context


class InstrumentoCreateView(CreateView):
    model = Instrumento
    form_class = InstrumentoForm
    template_name = 'form_instrumento.html'
    success_url = reverse_lazy('Instrumento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Insertar Instrumento'
        context['all_instrumento'] = Instrumento.objects.all()
        context['action'] = 'add'
        return context


class InstrumentoUpdateView(UpdateView):
    model = Instrumento
    form_class = InstrumentoForm
    template_name = 'form_instrumento.html'
    success_url = reverse_lazy('Instrumento-list')

    def get_context_data(self, **kwargs):
        context = super(InstrumentoUpdateView, self).get_context_data()
        context['title'] = 'Editar Instrumento'
        context['all_instrumento'] = Instrumento.objects.all()
        context['action'] = 'edit'
        return context


class InstrumentoDeleteView(DeleteView):
    model = Instrumento
    template_name = 'delete_instrumento.html'
    success_url = reverse_lazy('Instrumento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Instrumento'
        context['cancelar']=reverse_lazy('Instrumento-list')
        return context


