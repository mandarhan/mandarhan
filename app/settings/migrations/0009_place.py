# Generated by Django 2.2.7 on 2019-11-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_settings', '0008_interface'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('my_order', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='order')),
            ],
            options={
                'verbose_name': 'place',
                'verbose_name_plural': 'places',
                'ordering': ['my_order'],
            },
        ),
    ]
