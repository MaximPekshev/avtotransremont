from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible


class ContactForm(forms.Form):
	
	input_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
			'placeholder': 'Ваше имя *',
			'id': 'input_name',
			'autocomplete': 'off',
			'onCopy':'return false',
			'onDrag': 'return false',
			'onDrop': 'return false',
			'onPaste': 'return false',
		}))
	input_phone = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
			'placeholder': 'Телефон *',
			'id': 'input_phone',
			'onKeyPress': 'inputFilter()',
			'autocomplete': 'off',
			'onCopy':'return false',
			'onDrag': 'return false',
			'onDrop': 'return false',
			'onPaste': 'return false',
		}))
	input_comment = forms.CharField(max_length=5120, required=False, widget=forms.Textarea(attrs={
			'placeholder': 'Ваш комментарий',
			'id': 'input_comment',
			'autocomplete': 'off',
			'rows': '4',
		}))
	captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)