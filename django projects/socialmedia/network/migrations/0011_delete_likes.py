# Generated by Django 4.2.3 on 2023-08-21 18:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0010_remove_post_likes"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Likes",
        ),
    ]