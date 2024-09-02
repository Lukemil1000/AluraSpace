from django import forms

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