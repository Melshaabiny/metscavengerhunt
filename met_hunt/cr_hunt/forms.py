from django import forms
from cr_hunt.models import Items

class ItemForm(forms.ModelForm):
    clue = forms.CharField(label='Enter Clue:', max_length=250, help_text="Clue")
    item = forms.ModelChoiceField(label='Add Item', queryset=Items.objects.all(), help_text="Item")

    class Meta:
        model = Items
        fields = ('clue', 'item')
