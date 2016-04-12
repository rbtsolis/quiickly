from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import BranchOffice

def panel_index(request):

    if request.user.is_authenticated():

        print(request.user.id)

        user_sucursal = get_object_or_404(BranchOffice, user__id=request.user.id)

        data_template = {
            'branch_office' : user_sucursal
        }

        return render(request, 'principal.html', data_template)
    else:

        data_template = {
            'branch_office' : 0
        }

        return render(request, 'principal.html', data_template)
