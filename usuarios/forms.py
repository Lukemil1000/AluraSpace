from django import forms
from galeria.models import Fotografia

class LoginForms(forms.Form):
    
    nome = forms.CharField(
        label="Nome de login", 
        required=True, 
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: João Pedro"
            }
        )
    )

    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a senha"    
            }
        )
    )

class CadastroForms(forms.Form):
    
    nome=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Pedro',
            }
        )
    )

    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaopedro@xpto.com',
            }
        )
    )

    senha_1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )

    senha_2=forms.CharField(
        label='Confirme a sua senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',
            }
        ),
    )

    def clean_nome(self):
        nome = self.cleaned_data.get("nome")

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2
            
class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels = {
            'descricao':'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }