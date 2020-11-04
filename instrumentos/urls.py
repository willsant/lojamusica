from django.urls import path
from .views import list_instrumentos, create_instrumento, update_instrumento, delete_instrumento, paginacao_de_instrumento, index, cadastra_produto, atualiza_produto
from .forms import RecuperaInstrumentoForm

urlpatterns = [
    path('index/', index, name='index'),
    path('', list_instrumentos, name='list_instrumentos'),
    path('new', create_instrumento, name='create_instrumento'),
    path('update/<int:id>/', update_instrumento, name='update_instrumento'),
    path('delete/<int:id>/', delete_instrumento, name='delete_instrumento'),
    path('paginacao_de_instrumento/', paginacao_de_instrumento, name='paginacao_de_instrumento'),
    path('cadastra_produto/', cadastra_produto, name='cadastra_produto'),
    path('atualiza_produto/<int:id>', atualiza_produto, name='atualiza_produto'),

]