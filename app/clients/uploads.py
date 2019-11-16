from django.utils.crypto import get_random_string


def upload_client_photo(instance: object, filename: str) -> str:
    return 'client/%i/%s.%s' % (
        instance.client.id,
        get_random_string(),
        filename.split('.')[-1].lower()
    )


def upload_thumbnail(instance: object, filename: str) -> str:
    return 'client/%i/%s' % (
        instance.client.id,
        filename
    )
