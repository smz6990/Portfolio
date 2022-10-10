from django.forms import ModelForm
from simplemathcaptcha.fields import MathCaptchaField

from .models import Contact


class ContactForm(ModelForm):
    captcha = MathCaptchaField()

    class Meta:
        model = Contact
        fields = ['name', "email", "subject", "message", "captcha"]
