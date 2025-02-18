from django.shortcuts import render # type: ignore



def index(request):

    dados = {
    1: {'nome': 'Nebulosa de Carina', 
        'legenda': 'webbtelecope.org / NASA / James Webb'},
    2: {'nome': 'Galáxia NGC 1079',
        'legenda': 'nasa.org / Nasa / Hubble'}
}

    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')