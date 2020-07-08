from django.forms import ModelForm, forms

from medicines.models import Medicine


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'medicine_name',
            'medicine_info',
            'medicine_image',
            'medicine_qr',
            'medicine_code',
            'medicine_price',

        ]


class StockSearchForm(ModelForm):
    class Meta:
        model = Medicine
        fields = ['medicine_code', 'medicine_name', 'medicine_qr']


class StockCreateForm(ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'medicine_name',
            'medicine_info',
            'medicine_image',
            'medicine_code',
            'medicine_qr',
            'medicine_price',

        ]

    def clean_category(self):
        category = self.cleaned_data.get('medicine_code')
        if not category:
            raise forms.ValidationError('This field is required')
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('medicine_code')
        if not item_name:
            raise forms.ValidationError('This field is required')
        return item_name
