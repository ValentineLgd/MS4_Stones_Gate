from django import forms
from .models import Product, Category, Mood


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        moods = Mood.objects.all()
        moods_friendly_names = [(m.id, m.get_friendly_name()) for m in moods]

        self.fields['category'].choices = friendly_names
        self.fields['mood'].choices = moods_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
