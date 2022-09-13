# Generated by Django 4.1.1 on 2022-09-12 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_k", "0002_remove_post_userid_post_nickname_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="friendlist",
            old_name="username",
            new_name="friend",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="username",
        ),
        migrations.RemoveField(
            model_name="post",
            name="nickname",
        ),
        migrations.RemoveField(
            model_name="post",
            name="username",
        ),
        migrations.AddField(
            model_name="notification",
            name="created_by",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="who_created_post",
                to=settings.AUTH_USER_MODEL,
                verbose_name="投稿者",
            ),
        ),
    ]