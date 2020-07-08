from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify


class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    medicine_info = RichTextField(verbose_name="Details")
    medicine_image = RichTextField(verbose_name="Image")
    medicine_code = models.CharField(max_length=100)
    medicine_qr = models.CharField(max_length=100)
    medicine_price = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True, editable=False)

    def __str__(self):
        return self.medicine_name

    class Meta:
        ordering = ['medicine_name']

    def get_create_url(self):
        return reverse('medicines:medicine_create', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.slug.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Medicine.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def get_absolute_url(self):
        return reverse('medicines:medicine_create', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Medicine, self).save(*args, **kwargs)

