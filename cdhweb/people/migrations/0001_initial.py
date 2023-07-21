# Generated by Django 2.2.19 on 2021-05-03 16:46

import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cdhpages", "__first__"),
        ("wagtailcore", "0060_fix_workflow_unique_constraint"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wagtailimages", "0023_add_choose_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="PeopleLandingPage",
            fields=[
                (
                    "landingpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="cdhpages.LandingPage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cdhpages.landingpage",),
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=150, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=150, verbose_name="last name"),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "cdh_staff",
                    models.BooleanField(
                        default=False,
                        help_text="CDH staff or Postdoctoral Fellow.",
                        verbose_name="CDH Staff",
                    ),
                ),
                (
                    "job_title",
                    models.CharField(
                        blank=True,
                        help_text="Professional title, e.g. Professor or Assistant Professor",
                        max_length=255,
                    ),
                ),
                (
                    "department",
                    models.CharField(
                        blank=True,
                        help_text="Academic Department at Princeton or other institution",
                        max_length=255,
                    ),
                ),
                (
                    "institution",
                    models.CharField(
                        blank=True,
                        help_text="Institutional affiliation (for people not associated with Princeton)",
                        max_length=255,
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, help_text="Office phone number", max_length=50
                    ),
                ),
                (
                    "office_location",
                    models.CharField(
                        blank=True,
                        help_text="Office number and building",
                        max_length=255,
                    ),
                ),
                (
                    "pu_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("fac", "Faculty"),
                            ("stf", "Staff"),
                            ("graduate", "Graduate Student"),
                            ("undergraduate", "Undergraduate Student"),
                            ("external", "Not associated with Princeton"),
                        ],
                        default="",
                        max_length=15,
                        verbose_name="Princeton Status",
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        help_text="Corresponding user account for this person (optional)",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "people",
                "ordering": ("last_name",),
            },
        ),
        migrations.CreateModel(
            name="Position",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "person",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="positions",
                        to="people.Person",
                    ),
                ),
            ],
            options={
                "ordering": ["-start_date"],
            },
        ),
        migrations.CreateModel(
            name="Title",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, unique=True)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                (
                    "positions",
                    models.ManyToManyField(
                        through="people.Position", to="people.Person"
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "paragraph",
                                wagtail.blocks.RichTextBlock(
                                    features=[
                                        "h2",
                                        "h3",
                                        "h4",
                                        "bold",
                                        "italic",
                                        "link",
                                        "ol",
                                        "ul",
                                        "hr",
                                        "blockquote",
                                        "document",
                                        "superscript",
                                        "subscript",
                                        "strikethrough",
                                        "code",
                                    ]
                                ),
                            ),
                            (
                                "image",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        (
                                            "alternative_text",
                                            wagtail.blocks.TextBlock(
                                                help_text="Alternative text for visually impaired users to\nbriefly communicate the intended message of the image in this context.",
                                                required=True,
                                            ),
                                        ),
                                        (
                                            "caption",
                                            wagtail.blocks.RichTextBlock(
                                                features=[
                                                    "bold",
                                                    "italic",
                                                    "link",
                                                    "superscript",
                                                ],
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "svg_image",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.documents.blocks.DocumentChooserBlock(),
                                        ),
                                        (
                                            "alternative_text",
                                            wagtail.blocks.TextBlock(
                                                help_text="Alternative text for visually impaired users to\nbriefly communicate the intended message of the image in this context.",
                                                required=True,
                                            ),
                                        ),
                                        (
                                            "caption",
                                            wagtail.blocks.RichTextBlock(
                                                features=[
                                                    "bold",
                                                    "italic",
                                                    "link",
                                                    "superscript",
                                                ],
                                                required=False,
                                            ),
                                        ),
                                        (
                                            "extended_description",
                                            wagtail.blocks.RichTextBlock(
                                                features=["p"],
                                                help_text="This text will only be read to     non-sighted users and should describe the major insights or     takeaways from the graphic. Multiple paragraphs are allowed.",
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            ("embed", wagtail.embeds.blocks.EmbedBlock()),
                            (
                                "migrated",
                                wagtail.blocks.RichTextBlock(
                                    features=[
                                        "h3",
                                        "h4",
                                        "bold",
                                        "italic",
                                        "link",
                                        "ol",
                                        "ul",
                                        "hr",
                                        "blockquote",
                                        "document",
                                        "superscript",
                                        "subscript",
                                        "strikethrough",
                                        "code",
                                        "image",
                                        "embed",
                                    ],
                                    icon="warning",
                                ),
                            ),
                        ],
                        blank=True,
                    ),
                ),
                (
                    "attachments",
                    wagtail.fields.StreamField(
                        [
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(),
                            ),
                            (
                                "link",
                                wagtail.snippets.blocks.SnippetChooserBlock(
                                    "cdhpages.ExternalAttachment"
                                ),
                            ),
                        ],
                        blank=True,
                    ),
                ),
                ("education", wagtail.fields.RichTextField(blank=True)),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
                (
                    "person",
                    models.OneToOneField(
                        help_text="Corresponding person for this profile",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="people.Person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.AddField(
            model_name="position",
            name="title",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="people.Title"
            ),
        ),
        migrations.CreateModel(
            name="PersonRelatedLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField()),
                (
                    "person",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_links",
                        to="people.Person",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cdhpages.RelatedLinkType",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
