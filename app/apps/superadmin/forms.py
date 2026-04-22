from django import forms
from apps.cargo.models import CargoCompany
from apps.accounts.models import CustomUser


class CargoCompanyForm(forms.ModelForm):
    class Meta:
        model = CargoCompany
        fields = [
            'name', 'slug', 'logo', 'description',
            'phone', 'telegram', 'whatsapp', 'address', 'working_hours',
            'currency', 'bot_token', 'is_active',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название компании'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'url-slug'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+996 xxx xxx xxx'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@username'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+996 xxx xxx xxx'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'working_hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пн-Пт 9:00-18:00'}),
            'currency': forms.Select(attrs={'class': 'form-control'}),
            'bot_token': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Токен Telegram-бота'}),
        }


class ManagerCreateForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль'
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Подтверждение пароля'
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'cargo_company']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo_company': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('password_confirm')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Пароли не совпадают.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.MANAGER
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
