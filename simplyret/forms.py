from django import forms


class ConnectionForm(forms.Form):
    bs = forms.CharField(max_length=10, label='Номер сетевого элемента')
    login = forms.CharField(max_length=10, label='Имя пользователя ESC')
    password = forms.CharField(max_length=15, label='Пароль пользователя ESC')
    server = forms.ChoiceField(choices=[('ESC01', 'ESC01'), ('ESC02', 'ESC02'), ('ESC03', 'ESC03'), ('ESC04', 'ESC04'),
                                        ('ESC05', 'ESC05'), ('ESC06', 'ESC06'), ('ESC07', 'ESC07'), ('ESC08', 'ESC08'),
                                        ('ESC09', 'ESC09')], label='Сервер ESC')


class CheckingForm(forms.Form):
    bs = forms.CharField(max_length=10, label='Номер сетевого элемента')
