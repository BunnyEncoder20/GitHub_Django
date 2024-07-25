from django.shortcuts import render

# Create your views here.
def all_chai(request):
    return render(request, 'chai/chai_index.html')

def show_tailwind(request):
    return render(request,'chai/chai_tailwind.html')