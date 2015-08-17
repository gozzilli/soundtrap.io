from django import forms
from envelope.forms import ContactForm
from django.utils.translation import ugettext_lazy as _

class ModEnvelopeContactForm(ContactForm):
    
    sender = forms.CharField(label=_("Name"))
    email = forms.EmailField(label=_("Email"))
    subject = forms.CharField(label=_("Subject"), required=False, initial="I'm interested!")
    message = forms.CharField(label=_("Message"), widget=forms.Textarea(), required=False)