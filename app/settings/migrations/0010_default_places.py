from django.db import migrations

DEFAULT_PLACES = [
    {'name': 'номер'},
    {'name': 'комната'},
    {'name': 'квартира'},
    {'name': 'дом'},
    {'name': 'домик'},
    {'name': 'коттедж'},
    {'name': 'бунгало'},
    {'name': 'место'},
    {'name': 'беседка'},
    {'name': 'не определен'},
]


def create_default_places(apps, schema_editor):
    Place = apps.get_model('app_settings', 'Place')
    db_alias = schema_editor.connection.alias
    default_statuses = []
    order = 0
    for default_place in DEFAULT_PLACES:
        order += 1
        default_statuses.append(Place(**default_place, my_order=order))
    Place.objects.using(db_alias).bulk_create(default_statuses)


def delete_default_places(apps, schema_editor):
    Place = apps.get_model('app_settings', 'Place')
    db_alias = schema_editor.connection.alias
    for default_place in DEFAULT_PLACES:
        Place.objects.using(db_alias).filter(**default_place).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('app_settings', '0009_place'),
    ]

    operations = [
        migrations.RunPython(create_default_places, delete_default_places),
    ]
