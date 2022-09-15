from django.shortcuts import render

from .models import Projeto

# Create your views here.


def home_view(request):
    projetos = Projeto.objects.all().order_by('-id')
    return render(request, 'projetos/pages/base.html', context={
        'projetos': projetos,
    })
