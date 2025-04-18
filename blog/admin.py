from django.contrib import admin
from .models import Category, Article, AdSenseLocation, NewsletterSubscriber, SiteSettings

# Înregistrează modelele cu admin-ul standard Django
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(AdSenseLocation)
admin.site.register(NewsletterSubscriber)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """
Admin pentru setările site-ului.
    """
    fieldsets = (
        ('Informații de contact', {
            'fields': ('phone', 'email', 'address'),
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'instagram_url', 'youtube_url'),
        }),
        ('Secțiune Footer Despre', {
            'fields': ('footer_about_title', 'footer_about_text'),
        }),
    )

    def has_add_permission(self, request):
        """
Permite adăugarea doar dacă nu există deja o instanță.
        """
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """
Nu permite ștergerea setărilor site-ului.
        """
        return False
