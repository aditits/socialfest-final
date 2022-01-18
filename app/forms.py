from .models import Account

from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class AccountDetailsForm(forms.ModelForm):
    # Phone_Number = PhoneNumberField(
    #     widget = PhoneNumberPrefixWidget(attrs={'class': 'input-field'})
    # )
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}))

    def __init__(self, *args, **kwargs):
        super(AccountDetailsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input-field'

    class Meta:
        model = Account
        fields = ('Mobile_Number', 'Whatsapp_Number', 'Organisation', 'Publicity')