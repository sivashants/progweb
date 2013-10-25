from django import forms
class ConnexionForm(forms.Form):
	username = forms.CharField(label="Utilisateur",max_length=30)
	password = forms.CharField(label="mot de passe", widget = forms.PasswordInput)
