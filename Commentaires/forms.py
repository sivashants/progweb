from django import forms

class ConnexionForm(forms.Form):
	username = forms.CharField(label="Utilisateur",max_length=30)
	password = forms.CharField(label="mot de passe", widget = forms.PasswordInput)

class CommentsForm(forms.Form):
	
	titre = forms.CharField(label="titre",max_length=100)
	contenu = forms.CharField(label="votre commentaire",widget=forms.Textarea)
