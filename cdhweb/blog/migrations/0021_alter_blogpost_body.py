# Generated by Django 5.0.5 on 2024-07-04 23:03

import cdhweb.pages.blocks.download_block
import cdhweb.pages.blocks.migrated
import cdhweb.pages.blocks.newsletter
import cdhweb.pages.blocks.rich_text
import wagtail.blocks
import wagtail.contrib.typed_table_block.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_blogpost_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', cdhweb.pages.blocks.rich_text.RichTextBlock()), ('download_block', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='Heading for document block', max_length=80, required=False)), ('description', wagtail.blocks.TextBlock(help_text='A description to display with the download file (150 characters maximum).', max_length=150, required=False)), ('documents', wagtail.blocks.ListBlock(cdhweb.pages.blocks.download_block.FileBlock, help_text='Upload at least 1 and maximum 10 files. Each file size should be less than 5MB.', max_num=10, min_num=1))])), ('cta_block', wagtail.blocks.StructBlock([('introduction', wagtail.blocks.TextBlock(help_text='Short introduction to the action you want users to take. Ideal: 80 characters or less (Max: 100 characters).', max_length=100, required=False)), ('cta_buttons', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Button text', max_length=40, required=True))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock(label='Button text', max_length=40, required=True))]))], max_num=2, min_num=1))])), ('accordion_block', wagtail.blocks.StructBlock([('show_in_jumplinks', wagtail.blocks.BooleanBlock(default=False, help_text="Link to this block in the jumplinks list (when 'Show jumplinks' is enabled in Page settings)", required=False)), ('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=80, required=True))], required=False)), ('description', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=80, required=True, verbose_name='Accordion Title')), ('body', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul', 'document-link', 'h3', 'h4'], help_text='Only use H3 if you have not set an overall heading for the accordion block.'))])))])), ('video_block', wagtail.blocks.StructBlock([('video', wagtail.blocks.URLBlock(help_text='A YouTube URL. Link to a specifc video or playlist.')), ('accessibility_description', wagtail.blocks.CharBlock(help_text='Use this to describe the video. It is used as an accessibility attribute mainly for screen readers.', required=False)), ('transcript', wagtail.blocks.RichTextBlock(features=['bold', 'link', 'document-link'], required=False)), ('show_in_jumplinks', wagtail.blocks.BooleanBlock(default=False, help_text="Link to this block in the jumplinks list (when 'Show jumplinks' is enabled in Page settings)", required=False)), ('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=80, required=True))], required=False))])), ('hosted_video', wagtail.blocks.StructBlock([('show_in_jumplinks', wagtail.blocks.BooleanBlock(default=False, help_text="Link to this block in the jumplinks list (when 'Show jumplinks' is enabled in Page settings)", required=False)), ('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=80, required=True))], required=False)), ('video_url', wagtail.embeds.blocks.EmbedBlock(help_text='This should be used for videos from Princeton\'s Media Central. Copy the "oEmbed URL" from the "Share" menu')), ('accessibility_description', wagtail.blocks.CharBlock(help_text='Use this to describe the video. It is used as an accessibility attribute mainly for screen readers.', required=True)), ('transcript', wagtail.blocks.RichTextBlock(features=['bold', 'link', 'document-link'], required=False))])), ('pull_quote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.RichTextBlock(features=['bold', 'italic'], help_text='Pull a small section of content out as an "aside" to give it emphasis.', max_length=100, required=True)), ('attribution', wagtail.blocks.RichTextBlock(features=['bold', 'link'], help_text='Optional attribution', max_length=60, required=False))])), ('note', wagtail.blocks.StructBlock([('heading', wagtail.blocks.TextBlock(help_text='Optional heading', required=False)), ('message', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ul', 'ol'], help_text='Note message up to 750 chars', max_length=750, required=True))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('caption', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'link'], help_text='A short caption for the image.', max_length=180, required=False)), ('credit', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'link'], help_text='A credit line or attribution for the image.', max_length=80, required=False)), ('alt_text', wagtail.blocks.CharBlock(help_text='Describe the image for screen readers', max_length=80, required=False)), ('size', wagtail.blocks.ChoiceBlock(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], label='Image Size'))])), ('feature', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=80, required=True)), ('feature_text', wagtail.blocks.RichTextBlock(features=['bold', 'document-link', 'italic', 'link', 'ol', 'ul'], max_length=400)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('alt_text', wagtail.blocks.CharBlock(help_text='Describe the image for screen readers.', max_length=80, required=False)), ('cta_buttons', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Button text', max_length=40, required=True))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock(label='Button text', max_length=40, required=True))]))], max_num=2, min_num=0, required=False))])), ('table', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Table caption', label='Caption', required=False)), ('notes', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], help_text='Primarily for using for footnotes from cells with asterisks', label='Table notes', required=False)), ('table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('rich_text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul', 'h3']))], help_text='It is recommended to use a minimal number of columns, to ensure the table is usable on mobile and desktop.', max_num=1, min_num=1))])), ('newsletter', cdhweb.pages.blocks.newsletter.NewsletterBlock()), ('heading', wagtail.blocks.StructBlock([('show_in_jumplinks', wagtail.blocks.BooleanBlock(default=False, help_text="Link to this block in the jumplinks list (when 'Show jumplinks' is enabled in Page settings)", required=False)), ('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=80, required=True))]))])), ('tile_block', wagtail.blocks.StructBlock([('show_in_jumplinks', wagtail.blocks.BooleanBlock(default=False, help_text="Link to this block in the jumplinks list (when 'Show jumplinks' is enabled in Page settings)", required=False)), ('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=80, required=True))], help_text='Heading for this tile block', required=False)), ('description', wagtail.blocks.CharBlock(help_text='Description for this tile block', label='Description', required=False)), ('see_more_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(help_text='Choose a page to link to', label='Wagtail Page', required=False)), ('title', wagtail.blocks.CharBlock(help_text='Set title for this link', label='Link title', max_length=80, required=False))], help_text="'See more' link", required=False)), ('featured', wagtail.blocks.BooleanBlock(default=False, help_text='Check this checkbox to create a visually distinct tile block that stands out from regular tiles on the page.', required=False)), ('tiles', wagtail.blocks.StreamBlock([('internal_page_tile', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(required=True))])), ('external_page_tile', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title for this tile.', label='Tile Title', max_length=100, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image for this tile.', label='Tile Image', required=False)), ('summary', wagtail.blocks.CharBlock(help_text='Summary for this tile.', label='Tile Summary', max_length=200, required=False)), ('external_link', wagtail.blocks.URLBlock(required=True))]))], min_num=1, required=True))])), ('article_tile_block', wagtail.blocks.StructBlock([('show_in_jumplinks', wagtail.blocks.BooleanBlock(default=False, help_text="Link to this block in the jumplinks list (when 'Show jumplinks' is enabled in Page settings)", required=False)), ('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=80, required=True))], help_text='Heading for this tile block', required=False)), ('description', wagtail.blocks.CharBlock(help_text='Description for this tile block', label='Description', required=False)), ('landing_page', wagtail.blocks.PageChooserBlock(help_text='Select the Blog Landing Page whose child pages you want to show as tiles in this block.', page_type=['blog.BlogLandingPage'], required=True)), ('max_articles', wagtail.blocks.ChoiceBlock(choices=[(2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], help_text='Define the maximum number of tiles to show in this group.', icon='placeholder')), ('see_more_link', wagtail.blocks.CharBlock(default='See All', help_text='Set text for the link which takes you to the landing page', label='Link title', max_length=80, required=False))])), ('event_tile_block', wagtail.blocks.StructBlock([('show_in_jumplinks', wagtail.blocks.BooleanBlock(default=False, help_text="Link to this block in the jumplinks list (when 'Show jumplinks' is enabled in Page settings)", required=False)), ('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=80, required=True))], help_text='Heading for this tile block', required=False)), ('description', wagtail.blocks.CharBlock(help_text='Description for this tile block', label='Description', required=False)), ('landing_page', wagtail.blocks.PageChooserBlock(help_text='Select the Event Landing Page whose child pages you want to show as tiles in this block.', page_type=['events.EventsLandingPage'], required=True)), ('max_articles', wagtail.blocks.ChoiceBlock(choices=[(2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], help_text='Define the maximum number of tiles to show in this group.', icon='placeholder')), ('see_more_link', wagtail.blocks.CharBlock(default='See All', help_text='Set text for the link which takes you to the landing page', label='Link title', max_length=80, required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(help_text='This should be used for videos from Princeton\'s Media Central. Copy the "oEmbed URL" from the "Share" menu')), ('migrated', cdhweb.pages.blocks.migrated.MigratedBlock())], blank=True, help_text='Put content for the body of the page here. Start with using the + button.', use_json_field=True, verbose_name='Page content'),
        ),
    ]
