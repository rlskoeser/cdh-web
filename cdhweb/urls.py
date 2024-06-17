from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView, TemplateView
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps import Sitemap
from wagtail.contrib.sitemaps import views as sitemap_views
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.models import Page
from wagtailautocomplete.urls.admin import urlpatterns as autocomplete_admin_urls

from cdhweb.blog.sitemaps import BlogListSitemap
from cdhweb.context_processors import favicon_path
from cdhweb.events.sitemaps import EventListSitemap
from cdhweb.pages.views import OpenSearchDescriptionView, SiteSearchView
from cdhweb.people.sitemaps import PeopleListSitemap
from cdhweb.projects.sitemaps import ProjectListSitemap

admin.autodiscover()

# sitemap configuration for sections of the site
sitemaps = {
    "pages": Sitemap,  # wagtail content pages
    "people": PeopleListSitemap,
    "projects": ProjectListSitemap,
    "events": EventListSitemap,
    "blog": BlogListSitemap,
}


urlpatterns = [
    # wagtail autocompletes; must come before admin urls
    re_path(r"^cms/autocomplete/", include(autocomplete_admin_urls)),
    # admin site
    path("admin/", admin.site.urls),
    # special paths
    re_path(
        r"^robots\.txt$",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    re_path(
        r"^favicon\.ico$", RedirectView.as_view(url=favicon_path(), permanent=True)
    ),
    path("_500/", lambda _: 1 / 0),  # for testing 500 error page
    # main apps
    path("people/", include("cdhweb.people.urls", namespace="people")),
    path("blog/", include("cdhweb.blog.urls", namespace="blog")),
    path("events/", include("cdhweb.events.urls", namespace="event")),
    path("projects/", include("cdhweb.projects.urls", namespace="projects")),
    # search
    path("search/", SiteSearchView.as_view(), name="search"),
    path(
        "opensearch-description/",
        OpenSearchDescriptionView.as_view(),
        name="opensearch-description",
    ),
    # CAS login urls
    path("accounts/", include("pucas.cas_urls")),
    # sitemaps
    path(
        "sitemap.xml", sitemap_views.index, {"sitemaps": sitemaps}, name="sitemap-index"
    ),
    re_path(
        r"^sitemap-(?P<section>.+)\.xml$",
        sitemap_views.sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # wagtail paths
    path("cms/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # serve static files in development - automatically activates in DEBUG; see
    # https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

    # Serve 404 and 500 page templates(seeing as errors are masked with debug)
    urlpatterns.extend(
        [
            path("404/", TemplateView.as_view(template_name="404.html")),
            path("500/", TemplateView.as_view(template_name="500.html")),
        ]
    )
    try:
        import debug_toolbar

        # must come before wagtail catch-all route or else debug urls 404
        urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))
    except ImportError:
        pass

urlpatterns.append(
    # let wagtail handle everything else
    path("", include(wagtail_urls)),
)
