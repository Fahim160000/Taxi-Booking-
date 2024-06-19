from django import forms
from.models import TaxiDetails,Customer,PaymentReciept

class TaxiDetailsForm(forms.ModelForm):
    class Meta:
        model = TaxiDetails
        fields = ['registration_number','model','capacity','availability']
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number']
        
class PaymentRecieptForm(forms.ModelForm):
    class Meta:
        model = PaymentReciept
        fields = ['customer','taxi','amount']
                