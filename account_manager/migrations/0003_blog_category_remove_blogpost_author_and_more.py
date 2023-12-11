# Generated by Django 4.2.7 on 2023-12-11 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("account_manager", "0002_blogcategory_blogpost"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="blog_images/"),
                ),
                ("summary", models.TextField()),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_draft", models.BooleanField(default=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="author",
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="category",
        ),
        migrations.DeleteModel(
            name="BlogCategory",
        ),
        migrations.DeleteModel(
            name="BlogPost",
        ),
        migrations.AddField(
            model_name="blog",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="account_manager.category",
            ),
        ),
    ]
