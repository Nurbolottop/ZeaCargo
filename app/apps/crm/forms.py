from django import forms
from apps.orders.models import Order
from apps.clients.models import Client


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'client', 'track_number', 'shop', 'description',
            'weight', 'price_per_kg', 'delivery_status', 'payment_status', 'comment',
        ]
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'track_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CN2024110001'}),
            'shop': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Taobao, 1688...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001'}),
            'price_per_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'delivery_status': forms.Select(attrs={'class': 'form-control'}),
            'payment_status': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, *args, cargo_company=None, **kwargs):
        super().__init__(*args, **kwargs)
        if cargo_company:
            self.fields['client'].queryset = Client.objects.filter(
                cargo_company=cargo_company, is_active=True
            )
