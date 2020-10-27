from django import forms
class FormName(forms.Form):#just like models in django.
    name=forms.CharField(widget=forms.TextInput)#well default is TextInput but to add attributes its neccessary to do like this.
    email=forms.CharField(widget=forms.EmailInput)
    text=forms.CharField(widget=forms.Textarea(attrs={'id':'textr','placeholder':'testing'}))
    botcatcher=forms.CharField(widget=forms.HiddenInput(),required=False)
    def clean_botcatcher(self):# note that you cannot name this function randoemly. it has to be clean_fieldname.
        botcatcher=self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("gotcha a bot")
        return botcatcher
