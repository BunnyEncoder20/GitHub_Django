from django.shortcuts import render
from .models import ChaiTable

# Create your views here.
def all_chai(request):
    chai_list = ChaiTable.objects.all()
    return render(request, 'chai/chai_index.html', {'chai_list':chai_list})

def chai_details(request):
    pass

def show_tailwind(request):
    return render(request,'chai/chai_tailwind.html')