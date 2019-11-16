import os.path
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.safestring import mark_safe

from .uploads import upload_client_photo, upload_thumbnail


class Client(models.Model):
    SEX_CHOICES = (
        ('M', _('male')),
        ('F', _('female')),
    )

    # Основная информация
    last_name = models.CharField(_('last name'), max_length=160, null=True, blank=True)
    first_name = models.CharField(_('first name'), max_length=160)
    second_name = models.CharField(_('second name'), max_length=160, null=True, blank=True)
    additional_info = models.CharField(_('additional info'), max_length=255, null=True, blank=True)
    phone = models.CharField(_('phone'), max_length=32, null=True, blank=True)
    email = models.CharField(_('email'), max_length=255, null=True, blank=True)
    address = models.TextField(_('address'), null=True, blank=True)
    in_vip = models.BooleanField(_('in VIP list'), default=False)
    in_blacklist = models.BooleanField(_('in blacklist'), default=False)
    comment = models.TextField(_('comment'), null=True, blank=True)

    is_foreigner = models.BooleanField(_('is foreigner?'), default=False)
    sex = models.CharField(_('sex'), choices=SEX_CHOICES, max_length=1, blank=True)
    birthday = models.DateField(_('birthday'), null=True, blank=True)
    identification_doc = models.CharField(
        _('identification document name'), 
        max_length=160,
        null=True, 
        blank=True
    )
    doc_serial = models.CharField(_('document serial'), max_length=30, null=True, blank=True)
    doc_number = models.CharField(_('document number'), max_length=160, null=True, blank=True)
    doc_date = models.DateField(_('document date is issue'), null=True, blank=True)
    doc_issued_by = models.CharField(_('document issued by'), max_length=255, null=True, blank=True)

    added_at = models.DateTimeField(_('client added at'), default=timezone.now)

    class Meta:
        ordering = ['-added_at']
        verbose_name = _('client')
        verbose_name_plural = _('clients')

    def __str__(self):
        return self.full_name()

    def full_name(self):
        full_name = []
        if self.last_name:
            full_name.append(self.last_name)
        if self.first_name:
            full_name.append(self.first_name)
        if self.second_name:
            full_name.append(self.second_name)
        return ' '.join(full_name)

    full_name.short_description = _('full name')

    
class ClientPhotos(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_('client'))
    filename = models.CharField(max_length=255, editable=False)
    photo = models.ImageField(_('client photo'), upload_to=upload_client_photo)
    thumbnail = models.ImageField(_('photo preview'), upload_to=upload_thumbnail, editable=False)
    added_at = models.DateTimeField(_('photo added at'), default=timezone.now)
    my_order = models.PositiveSmallIntegerField(_('order'), default=0, )

    class Meta:
        ordering = ['my_order']
        verbose_name = _('client photo')
        verbose_name_plural = _('client photos')

    def __str__(self):
        return self.filename

    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            raise Exception('Could not create thumbnail - is the file type valid?')
        self.filename = self.photo.name
        super(ClientPhotos, self).save(*args, **kwargs)

    def make_thumbnail(self):
        image = Image.open(self.photo)
        size = 45, 45
        image.thumbnail(size, Image.ANTIALIAS)

        print('photo', self.photo)

        thumb_name, thumb_extension = os.path.splitext(self.photo.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = get_random_string() + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False

        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True

    def photo_preview(self):
        if self.photo:
            return mark_safe('<img src="%s" />' % self.thumbnail.url)
        else:
            return _('No photo')
    photo_preview.short_description = _('photo preview')
