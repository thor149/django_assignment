# Generated by Django 4.2.7 on 2023-12-11 12:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account_manager", "0006_category_alter_blogpost_image_post"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
        migrations.RemoveField(
            model_name="post",
            name="categories",
        ),
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]
