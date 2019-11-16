from django.db import migrations

_ = lambda s: s

DEFAULT_PAYMENTS = [
    {'name': 'Оплата при заселении'},
    {'name': 'Оплата онлайн'},
    {'name': 'Оплата по банковским реквизитам'},
    {'name': 'Наличные'},
    {'name': 'Банковская карта'},
]


def create_default_payments(apps, schema_editor):
    Payment = apps.get_model('app_settings', 'Payment')
    db_alias = schema_editor.connection.alias
    default_payments = []
    order = 0
    for default_payment in DEFAULT_PAYMENTS:
        order += 1
        default_payments.append(Payment(**default_payment, my_order=order))
    Payment.objects.using(db_alias).bulk_create(default_payments)


def delete_default_payments(apps, schema_editor):
    Payment = apps.get_model('app_settings', 'Payment')
    db_alias = schema_editor.connection.alias
    for default_payment in DEFAULT_PAYMENTS:
        Payment.objects.using(db_alias).filter(**default_payment).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('app_settings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_payments, delete_default_payments),
    ]
