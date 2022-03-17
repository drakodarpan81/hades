from django.forms import *
from app.erp.models import Category
from django.forms.widgets import NumberInput


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingresa un nombre',
                }
            ),
            'des': Textarea(
                attrs={
                    'placeholder': 'Ingresa una descripción',
                    'rows': 3,
                    'cols': 3
                }
            ),
            'fec': NumberInput(
                attrs={
                    'type': 'date'
                }
            )
        }
