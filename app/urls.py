from django.urls import path
from app.views import InstrumentoDeleteView, InstrumentoCreateView, InstrumentoUpdateView, InstrumentoDetailsView, \
    InstrumentoListView

urlpatterns = [

    path("", InstrumentoListView.as_view(), name='Instrumento-list'),
    path('create/', InstrumentoCreateView.as_view(), name='Instrumento-add'),
    path('update/<int:pk>/', InstrumentoUpdateView.as_view(), name='Instrumento-update'),
    path('delete/<int:pk>/', InstrumentoDeleteView.as_view(), name='Instrumento-delete'),
    path('details/<int:pk>/', InstrumentoDetailsView.as_view(), name='Instrumento-detail'),

]
