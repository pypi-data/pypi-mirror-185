from django.apps import AppConfig, apps
from django.contrib.auth import get_user_model
from django.db import DEFAULT_DB_ALIAS
from django.db.models.signals import post_migrate

from django_comment_migrate.db_comments import migrate_app_models_comment_to_database
from django_comment_migrate.utils import get_migrations_app_models


def handle_post_migrate(app_config, using=DEFAULT_DB_ALIAS, **kwargs):
    from django.contrib.auth.models import User

    migrations = (migration for migration, rollback in kwargs.get('plan', []) if not rollback)
    app_models = get_migrations_app_models(migrations, apps, using)
    # another user model is specified instead.
    if get_user_model() != User:
        app_models -= {User}
    migrate_app_models_comment_to_database(app_models, using)


class DjangoCommentMigrationConfig(AppConfig):
    name = "django_comment_migrate"

    def ready(self):
        post_migrate.connect(handle_post_migrate)
