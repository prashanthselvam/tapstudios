from django.forms import ModelForm, Textarea, TextInput
from .models import Message

class ContactForm(ModelForm):

	class Meta:
		model = Message
		fields = ('name','subject','email', 'text')
		error_css_class = 'error'
		required_css_class = 'required'
		widgets = {
            'name': TextInput(attrs={'placeholder': 'Name', 'class':'contact'}),
            'email': TextInput(attrs={'placeholder': 'Email', 'class':'contact'}),
            'subject': TextInput(attrs={'placeholder': 'Subject', 'class':'contact'}),
            'text': Textarea(attrs={'placeholder':'Message', 'class':'contact', 'rows':'5'})
        }