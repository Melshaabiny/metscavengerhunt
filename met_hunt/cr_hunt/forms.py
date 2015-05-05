from django import forms
from cr_hunt.models import Items

class ItemForm(forms.Form):
    clue = forms.CharField(label='Enter Clue:', max_length=250)
    item = forms.ModelChoiceField(label='Add Item:', queryset=Items.objects.all(), help_text="Item")

    
