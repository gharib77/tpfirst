from django import forms
from myblog.models import Produit,Etudient,Facture,Operation
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from django.forms.models import BaseModelFormSet
class EtudeForm(forms.ModelForm):
    date_entr = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y')
    )

    class Meta:
        model = Etudient
        fields = '__all__'


class ProduitForm(forms.ModelForm):
    dateprod = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y')
    )

    def clean(self):
        cleaned_data = super(ProduitForm, self).clean()
        for (k,v) in cleaned_data.items():
            print(k,v)

    
    class Meta:
        model = Produit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
        error_messages = {
            'libelle': {
                'required': "libelle obligatoire",
            },
            'prix': {
                'required': "prix obligatoire",
            },
        }


    

class FactureForm(forms.ModelForm):
    date_fact=forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y')
        )
    class Meta:
        model = Facture
        fields = '__all__'
class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        exclude = ['facture']


    def __init__(self, *args, **kwargs):
        super(OperationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    
        """ def save(self, commit=True):
                instance = super(OperationForm, self).save(commit=False)
                instance.qte=400
                if commit:
                    instance.save()
                return instance
        """   
        """ def clean(self):
            titles = []
            for form in self.formset:
                if self.can_delete and self._should_delete_form(form):
                    continue
                article = form.cleaned_data.get('article')
                if article in titles:
                    raise ValidationError("Articles in a set must have distinct titles.")
                titles.append(article)
    """    
