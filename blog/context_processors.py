from django.db.models import Count
from .models import Category, AdSenseLocation, SiteSettings

def global_context(request):
    # Obține doar categoriile care au cel puțin un articol
    categories = Category.objects.annotate(
        articles_count=Count('articles')
    ).filter(articles_count__gt=0)
    
    # Get AdSense locations
    adsense_locations = {
        ad.name: ad.ad_code for ad in AdSenseLocation.objects.filter(is_active=True)
    }
    
    # Get site settings
    try:
        site_settings = SiteSettings.objects.first()
    except:
        site_settings = None
    
    # Debug print
    print("Available AdSense locations:", adsense_locations.keys())
    
    return {
        'categories': categories,
        'adsense_locations': adsense_locations,
        'site_settings': site_settings
    }
