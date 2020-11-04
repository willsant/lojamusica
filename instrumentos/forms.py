from django import forms
from .models import Instrumento
from django.core.validators import RegexValidator
from decimal import Decimal

class RecuperaInstrumentoForm(forms.Form):
    buscaPor = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm texto'}),
        required=False)

class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ['nome', 'descricao', 'preco', 'quantidade']



class RemoveInstrumentoForm(forms.Form):
    class Meta:
        fields = ('instrumento_id')

    instrumento_id = forms.CharField(widget=forms.HiddenInput())


class ProdutoForm(forms.ModelForm):

    error_messages = {
        'campo_invalido': "Valor de preço inválido.",
        'descrcao_invalido': "A quantidade deve ser > zero.",
    }

    class Meta:
        model = Instrumento
        # O campo fields abaixo impede que seja atualizado um campo não especificado na lista abaixo. Deve ser especificado o
        # campo fields ou o campo exclude.
        fields = ('instrumento_id', 'nome', 'descricao', 'preco', 'quantidade')

    instrumento_id = forms.CharField(widget=forms.HiddenInput(), required=False)


    nome = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)
    descricao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)

    preco = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        min_length=4, validators=[RegexValidator(regex='^[0-9]{1,7}(,[0-9]{2})?$', message="Informe o preço no formato 9999999,99.")],
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                      'maxlength': '10',
                                      'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'}),
        required=True)

    quantidade = forms.IntegerField(
        min_value=0,
        max_value=1000,
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                      'maxlength': '20',
                                      'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'}),
        required=True)


    def clean_preco(self):
        preco = self.cleaned_data.get('preco')

        preco = Decimal(preco.replace(',', '.'))

        return preco

    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')

        if not quantidade:
            return quantidade

        if quantidade > 900:
            raise forms.ValidationError(
                self.error_messages['campo_invalido'], code='campo_invalido',
            )
        return quantidade






