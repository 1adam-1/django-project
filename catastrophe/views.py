from django.shortcuts import render
from .models import Catastrophe

def reco(request):
    selected_catastrophe_id = request.GET.get('selected_catastrophe')  # Retrieve the selected catastrophe ID from the GET request
    selected_catastrophe = None
    
    if selected_catastrophe_id:
        selected_catastrophe = Catastrophe.objects.get(pk=selected_catastrophe_id)
    
    return render(request, 'reco.html', {"cata": Catastrophe.objects.all(), "selected_catastrophe": selected_catastrophe})
