from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from soundtrap.settings import PROJ_NAME

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('%s admin' % PROJ_NAME )

    # Text to put in each page's <h1>.
    site_header = ugettext_lazy(PROJ_NAME)

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = MyAdminSite()