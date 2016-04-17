from django.shortcuts import render

def principal_store_view(request):
    return render(request, 'building.html')
