# Generated by Django 4.1.4 on 2023-06-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0010_alter_post_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
