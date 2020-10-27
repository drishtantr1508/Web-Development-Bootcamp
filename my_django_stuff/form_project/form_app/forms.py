from django import forms
#from form_app.models import User,Address
class FormName(forms.Form):
    First_name=forms.CharField(widget=forms.TextInput(attrs={'class':"inputname"}))
    Last_name=forms.CharField(widget=forms.TextInput(attrs={'class':"inputname"}))
    Email=forms.CharField(widget=forms.EmailInput(attrs={'class': "emailclass"}))
    contact=forms.IntegerField(widget=forms.TextInput(attrs={'class':"contactclass"}))
    Address=forms.CharField(widget=forms.TextInput(attrs={'class':"Addressclass"}))
    # class Meta():
    #     model = User
    #
    #     fields="__all__"
