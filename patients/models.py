from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Patient(models.Model):
    user = models.TextField(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    dept = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    notes = RichTextField(verbose_name="notes")
    slug = models.SlugField(max_length=100, unique=True, editable=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.first_name

    def get_create_url(self):
        return reverse('patients:patient_create', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.slug.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Patient.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def get_absolute_url(self):
        return reverse('patients:patient_create', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Patient, self).save(*args, **kwargs)

    class Meta:
        ordering = ['first_name']


