from django import forms


class ConnectionForm(forms.Form):
    bs = forms.CharField(max_length=9, label='Номер сетевого элемента')
    login = forms.CharField(max_length=15, label='Имя пользователя ENM')
    password = forms.CharField(max_length=15, label='Пароль пользователя ENM')
    server = forms.ChoiceField(choices=[('ENM6', 'ENM6'), ('ENM7', 'ENM7'), ('ENM8', 'ENM8'), ('ENM9', 'ENM9'),
                                        ('ENM10', 'ENM10'), ('ENM11', 'ENM11'), ('ENM12', 'ENM12'), ('ENM14', 'ENM14'),
                                        ('ENM15', 'ENM15')], label='Сервер ENM')


class CheckingForm(forms.Form):
    bs = forms.CharField(max_length=9, label='Номер сетевого элемента')
