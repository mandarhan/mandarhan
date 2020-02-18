import uuid


def category_uploader(instance, filename):
    return str('category/{}/{}.{}'.format(instance.id, uuid.uuid4(), filename.split('.')[-1]))


def room_uploader(instance, filename):
    return str('room/{}/{}.{}'.format(instance.id, uuid.uuid4(), filename.split('.')[-1]))
