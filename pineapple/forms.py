from django import forms
from .models import Subscription

class SellerForm:
    pass

class PineappleForm:
    pass

class OrderForm:
    pass

# AK/Subscription-form
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('09') or len(phone_number) != 11:
            raise forms.ValidationError(
                'شماره تلفن اشتباه است. شماره تلفن باید ۱۱ رقم باشد و با ۰۹ شروع شود.')

        return phone_number


class CommentForm:
    pass