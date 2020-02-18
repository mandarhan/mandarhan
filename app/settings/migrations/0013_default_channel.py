from django.db import migrations


def create_default_channel(apps, schema_editor):
    Channel = apps.get_model('app_settings', 'Channel')
    db_alias = schema_editor.connection.alias
    Channel.objects.using(db_alias).create(
        name='Стойка',
        my_order=1,
    )


def delete_default_channel(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('app_settings', '0012_channel'),
    ]

    operations = [
        migrations.RunPython(create_default_channel, delete_default_channel),
    ]
