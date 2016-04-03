from django.shortcuts import render
from django.http import Http404

from apps.api.tokens import decode_token
from apps.drugstores.models import BranchOffice
from apps.users.models import Quiickler
from .forms import OrderForm


def to_order(request):

    if request.method == "POST":

        product_id       = request.POST['product_id']
        token            = request.POST['token']
        address          = request.POST['address']
        branch_office_id = request.POST['branch_office_id']
        quiickler_id     = request.POST['quiickler_id']
        product_id       = request.POST['product_id']
        lattitude        = request.POST['lattitude']
        longitude        = request.POST['longitude']
        address          = request.POST['address']
        pay_method       = request.POST['pay_method']

        token_valid = decode_token(token)
        branch_office = BranchOffice.objects.get(id=branch_office_id)
        quiickler = Quiickler.objects.get(id=quiickler_id)
        product = Product.objects.get(id=product_id)

        if token_valid:
            if token_valid.id == request.user.id:

                user = User.objects.get(id=token_valid.id)
                order_form = OrderForm(
                    user,
                    address,
                    branch_office,
                    product,
                    quiickler,
                    lattitude,
                    longitude,
                    pay_method
                )


    else:
        return Http404



