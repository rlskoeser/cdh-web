# Generated by Django 2.2.17 on 2021-03-02 20:09

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('cdhpages', '0005_wagtailadmin_perms'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wagtailimages', '0022_uploadedimage'),
        ('blog', '0006_unproxy_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogLinkPage',
            fields=[
                ('linkpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cdhpages.LinkPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('cdhpages.linkpage',),
        ),
        migrations.CreateModel(
            name='BlogPostPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'blockquote', 'document', 'superscript', 'subscript', 'strikethrough', 'code'])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alternative_text', wagtail.core.blocks.TextBlock(help_text='Alternative text for visually impaired users to\nbriefly communicate the intended message of the image in this context.', required=True)), ('caption', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'superscript'], required=False))])), ('svg_image', wagtail.core.blocks.StructBlock([('image', wagtail.documents.blocks.DocumentChooserBlock()), ('alternative_text', wagtail.core.blocks.TextBlock(help_text='Alternative text for visually impaired users to\nbriefly communicate the intended message of the image in this context.', required=True)), ('caption', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'superscript'], required=False)), ('extended_description', wagtail.core.blocks.RichTextBlock(features=['p'], help_text='This text will only be read to     non-sighted users and should describe the major insights or     takeaways from the graphic. Multiple paragraphs are allowed.', required=False))])), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('migrated', wagtail.core.blocks.RichTextBlock(features=('a', 'abbr', 'acronym', 'address', 'area', 'article', 'aside', 'b', 'bdo', 'big', 'blockquote', 'br', 'button', 'caption', 'center', 'cite', 'code', 'col', 'colgroup', 'dd', 'del', 'dfn', 'dir', 'div', 'dl', 'dt', 'em', 'fieldset', 'figure', 'figcaption', 'font', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hr', 'i', 'img', 'input', 'ins', 'kbd', 'label', 'legend', 'li', 'map', 'men', 'nav', 'ol', 'optgroup', 'option', 'p', 'pre', 'q', 's', 'samp', 'section', 'select', 'small', 'span', 'strike', 'strong', 'sub', 'sup', 'table', 'tbody', 'td', 'textarea', 'tfoot', 'th', 'thead', 'tr', 'tt', '', 'ul', 'var', 'wbr', 'iframe'), icon='warning'))], blank=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_featured', models.BooleanField(default=False, help_text='Show the post in the carousel on the homepage.')),
                ('featured_image', models.ForeignKey(blank=True, help_text='Appears on the homepage carousel when post is featured.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('related_posts', models.ManyToManyField(blank=True, related_name='_blogpostpage_related_posts_+', to='blog.BlogPostPage')),
            ],
            options={
                'ordering': ('-first_published_at',),
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='BlogPostTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='blog.BlogPostPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_blogposttag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blogpostpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='blog.BlogPostTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
