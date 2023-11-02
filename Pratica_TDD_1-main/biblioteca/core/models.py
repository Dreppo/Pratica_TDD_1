from django.db import models

class LivroModel(models.Model):
    titulo = models.CharField('Título', max_length=200)
    editora = models.CharField('Editora', max_length=200)
    autor = models.CharField('Autor', null=True, max_length=200)
    isbn = models.CharField('ISBN', null=True, max_length=200)
    paginas = models.CharField('Número de Páginas', null=True, max_length=200)
    ano = models.CharField('Ano de Publicação', null=True, max_length=200)

    def __str__(self):
        return self.titulo