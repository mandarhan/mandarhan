from django.db import migrations

DEFAULT_STATUSES = [
    {
        'name': 'Не подтверждено',
        'color': '#ffffff',
    },
    {
        'name': 'Отменено',
        'color': '#ff0000',
    },
    {
        'name': 'Подтверждено',
        'color': '#daf9d3',
    },
    {
        'name': 'Выезд',
        'color': '#000000',
    },
    {
        'name': 'Незаезд',
        'color': '#1decf6',
    },
    {
        'name': 'Проживание',
        'color': '#048e08',
    },
    {
        'name': 'Резерв',
        'color': '#fff900',
    },
]


def create_default_statuses(apps, schema_editor):
    Status = apps.get_model('app_settings', 'Status')
    db_alias = schema_editor.connection.alias
    default_statuses = []
    order = 0
    for default_status in DEFAULT_STATUSES:
        order += 1
        default_statuses.append(Status(**default_status, my_order=order))
    Status.objects.using(db_alias).bulk_create(default_statuses)


def delete_default_statuses(apps, schema_editor):
    Status = apps.get_model('app_settings', 'Status')
    db_alias = schema_editor.connection.alias
    for default_status in DEFAULT_STATUSES:
        Status.objects.using(db_alias).filter(**default_status).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('app_settings', '0006_status'),
    ]

    operations = [
        migrations.RunPython(create_default_statuses, delete_default_statuses),
    ]
