from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/logar/')
def pacientes(request):
    return render(request, 'pacientes.html')
