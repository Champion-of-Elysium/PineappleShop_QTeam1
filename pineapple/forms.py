from django import forms
from .models import *


# AH/seller-form
class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'

    def clean_address(self):
        address = self.cleaned_data.get("address")
        if len(address) < 10:
            raise forms.ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")
        return address

    def clean_certificate_code(self):
        certificate_code = self.cleaned_data.get("certificate_code")
        if not certificate_code.isupper():
            raise forms.ValidationError("حروف گواهینامه باید حروف بزرگ باشد.")
        return certificate_code


# IDA/pineapple-form
class PineappleForm(forms.ModelForm):
    class Meta:
        model = Pineapple
        fields = '__all__'

    def clean_price_toman(self):
        price = self.cleaned_data.get('price_toman')
        if price < 1000:
            raise forms.ValidationError("قیمت نباید کمتر از هزار تومان باشد.")
        elif price > 1000000:
            raise forms.ValidationError("قیمت نباید از یک میلیون تومان بیشتر باشد.")
        return price


# Kia/order-Form
class OrderForm:
    class Meta:
        model = Order
        fields = "__all__"

    def clean_weight_kg(self):
        weight = self.cleaned_data.get("weight_kg")
        if weight > 100:
            raise forms.ValidationError("۱۰۰ کیلو آناناس میخوای چیکار؟ مشکل داری؟")
        return weight


# AK/subscription-form
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
