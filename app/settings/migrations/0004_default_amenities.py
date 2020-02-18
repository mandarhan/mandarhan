from django.db import migrations

DEFAULT_AMENITIES = [
    {
        'name': 'кондиционер',
        'code': 'conditioner',
    },
    {
        'name': 'телевизор',
        'code': 'tv',
    },
    {
        'name': 'Wi-Fi',
        'code': 'wifi',
    },
    {
        'name': 'мини-бар',
        'code': 'minibar',
    },
    {
        'name': 'сейф',
        'code': 'safe',
    },
    {
        'name': 'шкаф для одежды',
        'code': 'wardrobe',
    },
    {
        'name': 'электронный ключ',
        'code': 'card-key',
    },
    {
        'name': 'ванная комната',
        'code': 'bathroom',
    },
    {
        'name': 'душ',
        'code': 'shower',
    },
    {
        'name': 'холодильник',
        'code': 'refrigerator',
    },
    {
        'name': 'стиральная машина',
        'code': 'washer',
    },
    {
        'name': 'утюг',
        'code': 'iron',
    },
    {
        'name': 'фен',
        'code': 'hairdryer',
    },
    {
        'name': 'кухонная зона',
        'code': 'kitchen',
    },
    {
        'name': 'чайник',
        'code': 'teapot',
    },
    {
        'name': 'микроволновая печь',
        'code': 'microwave',
    },
    {
        'name': 'мультиварка',
        'code': 'slow-cooker',
    },
    {
        'name': 'электрическая плита',
        'code': 'electric-stove',
    },
    {
        'name': 'завтрак',
        'code': 'breakfast',
    },
    {
        'name': 'бассейн',
        'code': 'pool',
    },
    {
        'name': 'двуспальная кровать',
        'code': 'double-bed',
    },
    {
        'name': 'двухъярусная кровать',
        'code': 'bunk-bed',
    },
    {
        'name': 'диван',
        'code': 'sofa',
    },
    {
        'name': 'трансфер',
        'code': 'transfer',
    },
    {
        'name': 'номер для некурящих',
        'code': 'no-smoking',
    },
    {
        'name': 'с животными запрещено',
        'code': 'no-pets',
    },
    {
        'name': 'парковка',
        'code': 'parking',
    },
    {
        'name': 'балкон',
        'code': 'balcony',
    },
]


def create_default_ameities(apps, schema_editor):
    Amenity = apps.get_model('app_settings', 'Amenity')
    db_alias = schema_editor.connection.alias
    default_amenities = []
    order = 0
    for default_amenity in DEFAULT_AMENITIES:
        order += 1
        default_amenities.append(Amenity(**default_amenity, my_order=order))
    Amenity.objects.using(db_alias).bulk_create(default_amenities)


def delete_default_amenities(apps, schema_editor):
    Amenity = apps.get_models('app_settings', 'Amenity')
    db_alias = schema_editor.connection.alias
    for default_amenity in DEFAULT_AMENITIES:
        Amenity.objects.using(db_alias).filter(**default_amenity).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('app_settings', '0003_amenity')
    ]

    operations = [
        migrations.RunPython(create_default_ameities, delete_default_amenities),
    ]
