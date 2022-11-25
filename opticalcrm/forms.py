from django import forms
from .models import *
from django.core import validators
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm,PasswordResetForm

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-0 mt-4','placeholder':'*******'}))

class supplierForm(forms.ModelForm):
    class Meta:
        model = supplier_details
        fields= ("__all__")

class customer_detailsForm(forms.ModelForm):
    
    class Meta:
        model = customer_details
        fields = ("__all__")

class frameForm(forms.ModelForm):
    product_code=forms.CharField(max_length=5,min_length=5)
    def clean_product_code(self):
        data = self.cleaned_data["product_code"]
        if frame.objects.filter(product_code=data).exists():
            raise forms.ValidationError('That Product code is taken. Try another.')
        return data
    
    class Meta:
        model = frame
        fields = ("__all__")

class glassForm(forms.ModelForm):
    product_code=forms.CharField(max_length=5,min_length=5)

    def clean_product_code(self):
        data = self.cleaned_data["product_code"]
        if glass.objects.filter(product_code=data).exists():
            raise forms.ValidationError('That Product code is taken. Try another.')
        return data
    
    class Meta:
        model = glass
        fields = ("__all__")

class gogglesForm(forms.ModelForm):
    product_code=forms.CharField(max_length=5,min_length=5)

    def clean_product_code(self):
        data = self.cleaned_data["product_code"]
        if goggles.objects.filter(product_code=data).exists():
            raise forms.ValidationError('That Product code is taken. Try another.')
        return data
    
    class Meta:
        model = goggles
        fields = ("__all__")

class barcode_listForm(forms.ModelForm):
    barcode = forms.CharField(max_length=100,label="",)
    def clean_barcode(self):
        data = self.cleaned_data['barcode']
        
        if barcode_list.objects.filter(barcode = data).exists():
            raise forms.ValidationError('Invalid Barcode. please try another.')
        return data
    class Meta:
        model = barcode_list
        fields = ('barcode',)
