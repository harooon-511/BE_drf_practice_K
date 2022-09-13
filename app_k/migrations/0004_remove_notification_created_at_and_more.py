# Generated by Django 4.1.1 on 2022-09-12 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_k", "0003_rename_username_friendlist_friend_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notification",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="created_by",
        ),
        migrations.AddField(
            model_name="notification",
            name="post",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="which_post",
                to="app_k.post",
                verbose_name="ポスト",
            ),
        ),
    ]
