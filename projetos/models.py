from django.db import models


class Categoria(models.Model):
    stack = models.CharField(max_length=165)

    def __str__(self) -> str:
        return self.stack

# Create your models here.


class Projeto(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    link_projeto = models.CharField(max_length=1000)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)

    def is_valid(self):
        if self.categoria == "Python":
            return True
        return False

    def __str__(self) -> str:
        return self.title
