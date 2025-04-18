from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nume')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')  # Mărit la 200
    icon = models.CharField(max_length=50, blank=True, null=True, verbose_name='Iconiță FontAwesome')
    description = models.TextField(blank=True, null=True, verbose_name='Descriere')

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categorii'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titlu')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')  # Mărit la 200
    content = RichTextField(verbose_name='Conținut')
    featured_image = models.ImageField(upload_to='articles/', verbose_name='Imagine principală')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name='Categorie')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data creării')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data actualizării')
    read_time = models.IntegerField(default=5, verbose_name='Timp de citire (minute)')

    # SEO fields
    meta_title = models.CharField(max_length=200, blank=True, verbose_name='Titlu Meta')
    meta_description = models.TextField(blank=True, verbose_name='Descriere Meta')
    meta_keywords = models.CharField(max_length=200, blank=True, verbose_name='Cuvinte cheie Meta')

    class Meta:
        verbose_name = 'Articol'
        verbose_name_plural = 'Articole'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.meta_title:
            self.meta_title = self.title
        super().save(*args, **kwargs)


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# Define choices for AdSense locations
AD_LOCATION_CHOICES = [
    ('below_header', 'Sub Antet (Liste)'),
    ('before_footer', 'Înainte de Footer'),
    ('above_content', 'Deasupra Conținut Articol'),
    ('below_content', 'Sub Conținut Articol'),
    ('below_hero', 'Sub Secțiunea Hero (Homepage)'),
    ('middle_page', 'Mijloc Pagină (Homepage)'),
]

class AdSenseLocation(models.Model):
    name = models.CharField(
        max_length=100,
        choices=AD_LOCATION_CHOICES,
        unique=True, # Ensure only one entry per location
        verbose_name='Nume locație'
    )
    ad_code = models.TextField(verbose_name='Cod AdSense', help_text="Codul complet <script>...</script> sau <ins>...</ins> de la AdSense.")
    is_active = models.BooleanField(default=True, verbose_name='Este activ')

    class Meta:
        verbose_name = 'Locație AdSense'
        verbose_name_plural = 'Locații AdSense'
        ordering = ['name']

    def __str__(self):
        # Return the human-readable name from choices
        return self.get_name_display()


class SiteSettings(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Telefon', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)
    address = models.TextField(verbose_name='Adresă', blank=True)
    facebook_url = models.URLField(verbose_name='Link Facebook', blank=True)
    instagram_url = models.URLField(verbose_name='Link Instagram', blank=True)
    youtube_url = models.URLField(verbose_name='Link YouTube', blank=True)

    # Adăugăm câmpurile pentru footer
    footer_about_title = models.CharField(max_length=100, default="Despre noi", verbose_name="Titlu secțiune despre")
    footer_about_text = models.TextField(default="Blogul nostru este dedicat pasionaților de fitness și nutriție care caută informații de calitate pentru un stil de viață sănătos.", verbose_name="Text secțiune despre")

    class Meta:
        verbose_name = 'Setări Site'
        verbose_name_plural = 'Setări Site'

    def __str__(self):
        return 'Setări site'

    @classmethod
    def get_settings(cls):
        """Returnează setările site-ului sau creează o instanță dacă nu există."""
        settings, created = cls.objects.get_or_create(pk=1)
        return settings
