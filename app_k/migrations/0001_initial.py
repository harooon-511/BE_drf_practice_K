# Generated by Django 4.1.1 on 2022-09-20 20:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("email", models.EmailField(max_length=50, unique=True, verbose_name="Email")),
                ("nickname", models.CharField(default=0, max_length=10, verbose_name="ニックネーム")),
                (
                    "username",
                    models.CharField(
                        max_length=10,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(5),
                            django.core.validators.RegexValidator("^[a-zA-Z0-9]*$"),
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now, verbose_name="登録日"),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "db_table": "Users",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("content", models.TextField(max_length=128, verbose_name="今何してる？")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="投稿日時")),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="when_created_post",
                        to=settings.AUTH_USER_MODEL,
                        to_field="username",
                        verbose_name="投稿者",
                    ),
                ),
            ],
            options={
                "db_table": "Posts",
            },
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "post",
                    models.OneToOneField(
                        default=0,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="which_post",
                        to="app_k.post",
                        verbose_name="ポスト",
                    ),
                ),
            ],
            options={
                "db_table": "Notifications",
            },
        ),
        migrations.CreateModel(
            name="Friendlist",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("read_at", models.DateTimeField(auto_now_add=True, verbose_name="友達になった日")),
                (
                    "reader",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="who_met_before",
                        to=settings.AUTH_USER_MODEL,
                        to_field="username",
                        verbose_name="読んだ人",
                    ),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to=settings.AUTH_USER_MODEL,
                        to_field="username",
                        verbose_name="読まれた人",
                    ),
                ),
            ],
            options={
                "db_table": "Friendlists",
            },
        ),
    ]
