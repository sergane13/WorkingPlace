# Generated by Django 2.1.15 on 2021-01-26 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_opinions_idea_opinion'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinions',
            name='idea_opinion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Idea'),
            preserve_default=False,
        ),
    ]
