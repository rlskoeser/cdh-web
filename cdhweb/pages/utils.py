from django.contrib.sites.models import Site
from django.forms.widgets import TextInput


def absolutize_url(local_url):
    """Convert a local url to an absolute url, with scheme and server name,
    based on the current configured :class:`~django.contrib.sites.models.Site`.

    :param local_url: local url to be absolutized, e.g. something generated by
        :meth:`~django.core.urlresolvers.reverse`
    """
    if local_url.startswith("https"):
        return local_url

    # add scheme and server (i.e., the http://example.com) based
    # on the django Sites infrastructure.
    root = Site.objects.get_current().domain
    # but also add the http:// if necessary, since most sites docs
    # suggest using just the domain name
    # NOTE: this is problematic for dev/test sites without https
    if not root.startswith("https"):
        root = "https://" + root

    # make sure there is no double slash between site url and local url
    if local_url.startswith("/"):
        root = root.rstrip("/")

    return root + local_url


class LengthOverrideWidget(TextInput):
    """
    Enforce a client-side text length limit in a widget

    This can be used in conjuction with a Wagtail fieldpanel
    to allow a limit to be enforced without making changes
    to the Page model - particularly useful for the title
    field.

    Usage:
        content_panels = [
            FieldPanel(
                "title",
                widget=LengthOverrideWidget(max_length=70),
            ),
            ...
        ]
    """

    def __init__(self, attrs=None, max_length=None):
        super().__init__(attrs)
        self.max_length = max_length

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["attrs"]["maxlength"] = self.max_length
        return context
