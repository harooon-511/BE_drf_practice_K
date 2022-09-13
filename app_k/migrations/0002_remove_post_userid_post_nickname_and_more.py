# Generated by Django 4.1.1 on 2022-09-12 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_k", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="userid",
        ),
        migrations.AddField(
            model_name="post",
            name="nickname",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nickname_created_post",
                to=settings.AUTH_USER_MODEL,
                verbose_name="ニックネーム",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="nickname",
            field=models.CharField(default=0, max_length=10, verbose_name="ニックネーム"),
        ),
        migrations.AlterField(
            model_name="friendlist",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="who_met_before",
                to=settings.AUTH_USER_MODEL,
                verbose_name="ユーザーネーム",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="who_created_post",
                to=settings.AUTH_USER_MODEL,
                verbose_name="ユーザーネーム",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="when_created_post",
                to=settings.AUTH_USER_MODEL,
                verbose_name="投稿者",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="username_created_post",
                to=settings.AUTH_USER_MODEL,
                verbose_name="ユーザーネーム",
            ),
        ),
    ]
