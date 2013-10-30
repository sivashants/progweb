from django import forms

from models import Movie_Comments,Serie_Comments
class ConnexionForm(forms.Form):
	username = forms.CharField(label="Utilisateur",max_length=30)
	password = forms.CharField(label="mot de passe", widget = forms.PasswordInput)

class MovieCommentsForm(forms.ModelForm):
	
	class Meta:
		model=Movie_Comments
		exclude=('author','movie')

class SerieCommentsForm(forms.ModelForm):
	
	class Meta:
		model=Serie_Comments
		exclude=('author','serie')
