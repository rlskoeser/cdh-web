# Generated by Django 2.2.19 on 2021-03-17 20:53

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_no_body_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='old_project',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.OldProject'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='project',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grants', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='old_project',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.OldProject'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='project',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='memberships', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='projectrelatedlink',
            name='old_project',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.OldProject'),
        ),
        migrations.AlterField(
            model_name='projectrelatedlink',
            name='project',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_links', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='projecttag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='projects.Project'),
        ),
    ]
