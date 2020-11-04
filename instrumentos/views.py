from django.shortcuts import render, redirect
from .models import Instrumento
from .forms import InstrumentoForm, RecuperaInstrumentoForm, ProdutoForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def list_instrumentos(request):
    instrumentos = Instrumento.objects.all()
    return render(request, 'instrumentos.html', {'instrumentos': instrumentos})

def create_instrumento(request):
    form = InstrumentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_instrumentos')

    return render(request, 'instrumentos-form.html', {'form': form})

def update_instrumento(request, id):
    instrumento = Instrumento.objects.get(id=id)
    form = InstrumentoForm(request.POST or None, instance=instrumento)
    if form.is_valid():
        form.save()
        return redirect('list_instrumentos')

    return render(request, 'instrumentos-form.html', {'form': form, 'instrumento': instrumento})

def delete_instrumento(request, id):
    instrumento = Instrumento.objects.get(id=id)

    if request.method == 'POST':
        instrumento.delete()
        return redirect('list_instrumentos')

    return render(request, 'inst-delete-form.html', {'instrumento': instrumento})

def paginacao_de_instrumento(request):

    recupera_instrumento_form = RecuperaInstrumentoForm(request.GET)

    # print("recupera_fiscalizado_form = ", recupera_fiscalizado_form)
    if recupera_instrumento_form.is_valid():
        pass
    buscaPor = recupera_instrumento_form.cleaned_data['buscaPor']

    lista_de_instrumentos = Instrumento.objects.filter(nome__icontains=buscaPor).order_by('nome')
    # Cria um objeto paginator que irá provocar a execução de uma query que irá
    # retornar apenas os produtos de uma determinada página.
    pagina = request.GET.get('pagina', 1)
    paginator = Paginator(lista_de_instrumentos, 3)
    print("paginator.num_pages = ", paginator.num_pages)
    try:
        instrumentos = paginator.page(pagina)
    except PageNotAnInteger:
        instrumentos = paginator.page(1)
    except EmptyPage:
        instrumentos= paginator.page(paginator.num_pages)

    return render(request, 'paginacao.html', {'form': recupera_instrumento_form,
                                                            'instrumentos': instrumentos,
                                                            'buscaPor': buscaPor
                                                            })


def index(request):
    #user_list = Instrumento.objects.all()
    #page = request.GET.get('page', 1)

    #paginator = Paginator(user_list, 2)
    #try:
        #instrumentos = paginator.page(page)
    #except PageNotAnInteger:
        #instrumentos = paginator.page(1)
    #except EmptyPage:
        #instrumentos = paginator.page(paginator.num_pages)

    return render(request, 'index.html')

def atualiza_produto(request, id, num):
    instrumento = Instrumento.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=instrumento)
    if form.is_valid():
        form.save()
        return redirect('cadastro_produto')

    return render(request, 'cadastra_instrumento.html', {'form': form, 'instrumento': instrumento})


def cadastra_produto(request):

    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():
            instrumento = form.save(commit=False)
            instrumento.user = request.user
            instrumento.save()

            #return redirect('cadastra_produto')
    else:
        form = ProdutoForm()

    instrumentos = Instrumento.objects.all()

    valor_de_quantidade = 0
    lista = []
    ids_dos_instrumentos = []
    for instrumento in instrumentos:
        valor_de_quantidade = valor_de_quantidade + instrumento.preco * instrumento.quantidade
        ids_dos_instrumentos.append(instrumento.id)
        lista.append({'instrumento': instrumento,
                       # 'remove_produto_form': RemoveProdutoForm(initial={'produto_id': produto.id}),
                      'pode_remover': True if instrumento.user == request.user else False})

    return render(request, 'cadastra_instrumento.html', {'form': form,
                                                            'lista': lista,
                                                            'valor_de_quantidade': valor_de_quantidade,
                                                            'ids_dos_instrumentos': ids_dos_instrumentos})
# Create your views here.


class LoginRequiredMiddleware(object):
    """
    Require Login middleware. If enabled, each Django-powered page will require authentication.
    If an anonymous user requests a page, the user is redirected to the login page set by LOGIN_URL.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.login_path = getattr(settings, 'LOGIN_URL')

        print("init - get_response = ", get_response)
        print("init - login_path = ", self.login_path)

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print("request.path = ", request.path)
        print("self.login_path = ", self.login_path)
        print("request.user.is_anonymous = ", request.user.is_anonymous)

        if request.path != self.login_path and request.user.is_anonymous:
            return HttpResponseRedirect('%s?next=%s' % (self.login_path, request.path))

        response = self.get_response(request)

        # print("response = ", response)

        # Code to be executed for each request/response after
        # the view is called.

        return response
