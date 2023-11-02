from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel
from core.data import ano_atual


def validate_title(value):
    if len(value) < 3:
        raise ValidationError('O nome do livro deve ter pelo menos 3 caracteres')
    elif len(value) > 10:
        raise ValidationError('O nome do livro deve ter no máximo 10 caracteres')
    
def validate_editora(value):
    if len(value) < 3:
        raise ValidationError('O nome da editora deve ter pelo menos 3 caracteres')
    elif len(value) > 10:
        raise ValidationError('O nome da editora deve ter no máximo 10 caracteres')
    
def validate_autor(value):
    if len(value) < 10:
        raise ValidationError('O nome do autor deve ter pelo menos 3 caracteres')

def validate_ISBN(value):
    if value.isdigit() == False:
        raise ValidationError('O ISBN deve ser numérico')
    else:
        if len(value) != 13:
            raise ValidationError('O ISBN deve ter 13 caracteres')
        
def validate_paginas(value):
    if value.isdigit()== False:
        raise ValidationError('O número de páginas deve ser numérico')
    else:
        if int(value) < 1 or int(value) > 999:
            raise ValidationError('O número de páginas deve ter de 1 a 3 digitos')
        elif int(value) < 1 and int(value) > 0:
            raise ValidationError('O número de páginas deve ser maior que ZERO')
        
def validate_data(value):
    value = int(value)
    if ano_atual < value:
       raise ValidationError('O ano de publicação deve ser menor ou igual a {0}'.format(ano_atual))
        
def validate_ano(value):
    if value.isdigit() == False:
        raise ValidationError('O ano deve ser numérico')
    else:
        if len(value) < 4:
            raise ValidationError('O ano deve ter 4 digitos')

class LivroForm(forms.ModelForm):

    class Meta:
        model = LivroModel
        fields = ['titulo', 'editora', 'autor', 'isbn', 'paginas', 'ano']
        error_messages = {
            'titulo': {
                'required': ("Informe o título do livro."),
            },
            'editora': {
                'required': ("Informe a editora do livro."),
            },
            'autor': {
                'required': ("Informe o autor do livro."),
            },
            'isbn': {
                'required': ("Informe o ISBN do livro."),
            },
            'paginas': {
                'required': ("Informe o número de páginas do livro."),
            },
            'ano':{
                'required': ("Informe o ano de publicação do livro."),
            },
        }

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data  

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_title(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_title(editora)
        return editora
    
    def clean_autor(self):
        autor = self.cleaned_data['autor']
        validate_autor(autor)
        return autor
    
    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        validate_ISBN(isbn)
        return isbn
    
    def clean_paginas(self):
        paginas = self.cleaned_data['paginas']
        validate_paginas(paginas)
        return paginas
    
    def clean_ano(self):
        ano = self.cleaned_data['ano']
        validate_ano(ano)
        validate_data(ano)
        return ano

    

