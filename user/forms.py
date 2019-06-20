from django import forms
from sozlukContent.models import SozlukContent
from django.contrib.auth.models import User

class WordForm(forms.ModelForm):

    class Meta:
        model = SozlukContent
        fields = [
            'orn',
            'ekleyen',
            'artikel',
            'kategori',
            'plural_wort_status',
            'asw_de',
            'asw_tr',
            'tr',
            'en',
            'de',
            'referans_video',
            'tr_def',
            'de_def',
            'active',
            'ekleyenId',
            'abz_de',
            'abz_tr',
            'synm_de',
            'synm_tr',
            'anmerkungen_de',
            'anmerkungen_tr',
            'kontext_de',
            'kontext_tr',
        ]



class LoginForm(forms.Form):

    username=forms.CharField(max_length=150,label='Kullanıcı Adı')
    password=forms.CharField(max_length=150,label='Parola',widget=forms.PasswordInput)



class RegisterForm(forms.ModelForm):
    nameSurname=forms.CharField(max_length=150,label='Ad Soyad')
    username=forms.CharField(max_length=150,label='Kullanıcı Adı')
    email=forms.EmailField(max_length=150,label='Email',widget=forms.EmailInput)
    password1=forms.CharField(max_length=150,label='Parola',widget=forms.PasswordInput)
    password2=forms.CharField(max_length=150,label='Parola',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=[
            'username',
            'password1',
            'password2',
            'nameSurname',
            'email',
            
        ]


    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parololar eşleşmiyor")
        else:
            return password2
    
    
