# Generated by Django 2.2.7 on 2019-11-25 07:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0002_auto_20181220_0803'),
        ('app_settings', '0010_default_places'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('preferences_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='preferences.Preferences')),
                ('name', models.CharField(default='ООО "5 звезд"', max_length=128, verbose_name='name')),
                ('address', models.TextField(default='Россия, Москва', verbose_name='address')),
                ('email', models.EmailField(default='info@mandarhan.com', max_length=254, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=128, null=True, verbose_name='phone')),
                ('rules', models.TextField(blank=True, help_text='displayed in the reservation module', null=True, verbose_name='terms and conditions of booking')),
                ('time_in', models.TimeField(default=datetime.time(13, 0), verbose_name='Время заезда по умолчанию')),
                ('time_out', models.TimeField(default=datetime.time(12, 0), verbose_name='Время выезда по умолчанию')),
                ('bank_detail_recipient', models.CharField(default='ООО "5 звезд"', max_length=255, verbose_name='Получатель платежа')),
                ('bank_detail_inn', models.CharField(default='123456789', max_length=12, verbose_name='ИНН')),
                ('bank_detail_kpp', models.CharField(blank=True, default='123456789', max_length=9, null=True, verbose_name='КПП')),
                ('bank_detail_account', models.CharField(default='12345678912345678912', max_length=25, verbose_name='Номер счета')),
                ('bank_detail_bank_name', models.CharField(default='Сбербанк', max_length=255, verbose_name='Банк')),
                ('bank_detail_bik', models.CharField(default='123456', max_length=9, verbose_name='БИК')),
                ('bank_detail_cor_account', models.CharField(default='12345678912345678912', max_length=25, verbose_name='Корреспондентский счёт')),
                ('place', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app_settings.Place', verbose_name='place type')),
            ],
            options={
                'verbose_name': 'объект размещения',
                'verbose_name_plural': 'объекты размещения',
            },
            bases=('preferences.preferences',),
            managers=[
                ('singleton', django.db.models.manager.Manager()),
            ],
        ),
    ]