"""Exodus script for blog posts."""
import logging

from mezzanine.core.models import CONTENT_STATUS_PUBLISHED

from cdhweb.blog.models import Author, BlogLinkPage, BlogPost, OldBlogPost
from cdhweb.pages.exodus import (convert_slug, exodize_attachments, exodize_history,
                                 get_wagtail_image, to_streamfield)
from cdhweb.people.models import Person


def blog_exodus():
    """Exodize all blog models."""
    # get the top-level blog link page
    try:
        blog_link = BlogLinkPage.objects.get()
    except BlogLinkPage.DoesNotExist:
        logging.error("no blog link page; aborting blog exodus")
        return

    # create new blog posts
    for post in OldBlogPost.objects.all():
        logging.debug("found mezzanine blogpost %s" % post)

        # create page
        post_page = BlogPost(
            title=post.title,
            slug=convert_slug(post.slug),
            featured=post.is_featured,
            # NOTE use autogenerated description because get_description() won't
            # generate one if the body content is of type "migrated", so we need
            # to populate it
            description=post.description,
            search_description=post.description,
            body=to_streamfield(post.content),
            featured_image=get_wagtail_image(post.featured_image)
        )

        # add it as a child of blog landing page so slugs are correct
        blog_link.add_child(instance=post_page)
        blog_link.save(log_action=False)

        # if the old post wasn't published, unpublish the new one
        if post.status != CONTENT_STATUS_PUBLISHED:
            post_page.unpublish(log_action=False)

        # set publication dates
        post_page.first_published_at = post.publish_date
        post_page.last_published_at = post.updated
        post_page.save(log_action=False)

        # transfer authors
        for user in post.users.all():
            person = Person.objects.get(user=user)
            Author.objects.create(person=person, post=post_page)

        # transfer attachments
        exodize_attachments(post, post_page)
        exodize_history(post, post_page)

        # NOTE no tags to migrate
