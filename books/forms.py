# All forms class for the Book app goes here.
from django import forms



class ContactForm(forms.Form):
	"""
	Using Django forms.
	"""
	# maxlength defines a built in validation logic.
	subject = forms.CharField(max_length=20)

	# An EmailField has built in validation logic, which tells the 
	# client to include '@' and contains characters both in front of
	# and after the '@' symbol.
	email = forms.EmailField(required=False)

	# CharField is the type, but widget is the presentation logic,
	# which tells the browser to create a area specialized for large
	# amount of text input.
	message = forms.CharField(widget=forms.Textarea)



	def clean_message(self):
		"""
		The method to further validate and transform the 'message'
		field after the field has been validated by Django forms' built
		in validation logic.
		"""
		message = self.cleaned_data['message']

		# Make sure the message has at least 3 words. If not, then
		# raise a validation error.
		num_words = len(message.split())
		if num_words < 3:
			raise forms.ValidationError('There should be at least 3 words.')

		return message



	def clean_subject(self):
		"""
		For the 'subject' field. Here we just change the field value.
		"""
		return 'client subject: ' + self.cleaned_data['subject']
