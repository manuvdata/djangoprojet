from django import forms


from .models import Anniversaire

class AnnivForm(forms.ModelForm):
    class Meta:
        model = Anniversaire
        fields = ('pdf',)
