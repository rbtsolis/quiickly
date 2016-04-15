from django import forms


from .models import Address


'''
class CreateUserForm(forms.Form):

    display_name = forms.CharField(max_length=50)
    email        = forms.EmailField(unique=True, blank=False, null=False)
    avatar       = forms.ImageField()
    phone        = forms.IntegerField()
    address      = forms.ModelMultipleChoiceField()
    os           = forms.CharField(max_length=50)
'''

class AddressForm(forms.ModelForm):

    name      = forms.CharField(max_length=50)
    address   = forms.CharField(max_length=50)
    latitude  = forms.DecimalField(max_digits=20, decimal_places=5)
    longitude = forms.DecimalField(max_digits=20, decimal_places=5)

