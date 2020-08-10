from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Pagina de Inicio dependiendo el rol del usuario redireccionara a una pagina... ")
    return render(request, 'home.html')

def prospecto(request):
    #return HttpResponse("Pagina de Prospectos")
    return render(request, 'prospecto.html')

def oportunidad(request):
    #return HttpResponse("Pagina de Oportunidades")
    return render(request, 'oportunidad.html')

def pedido(request):
    #return HttpResponse("Pagina de Pedidos")
    return render(request, 'pedido.html')
