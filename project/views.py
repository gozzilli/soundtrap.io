from envelope.views import ContactView as EnvContactView
from braces.views import FormMessagesMixin
from django.core.urlresolvers import reverse_lazy
from project.forms import ModEnvelopeContactForm


class ContactView(FormMessagesMixin, EnvContactView):
    
    form_class = ModEnvelopeContactForm
     
    template_name = "project/contact.html"
    success_url = reverse_lazy('contact')
    
    form_valid_message = (u"Thank you for your message.")
    form_invalid_message = (u"There was an error in the contact form.")