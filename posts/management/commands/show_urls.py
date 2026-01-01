from django.core.management.base import BaseCommand
from django.urls import URLResolver, URLPattern, get_resolver


def list_urls(urlpatterns, parent='', app_source=''):
    """
    Recursively traverse URL patterns to collect full URL, name, and app source.
    """
    urls = []
    for x in urlpatterns:
        if isinstance(x, URLPattern):
            full_path = parent + str(x.pattern)
            urls.append({
                'url': full_path,
                'name': x.name or '',
                'app': app_source
            })
        elif isinstance(x, URLResolver):
            # Determine app name from the module path
            new_app = x.urlconf_module.__name__.split('.')[0] if hasattr(x.urlconf_module, '__name__') else ''
            full_path = parent + str(x.pattern)
            urls += list_urls(x.url_patterns, parent=full_path, app_source=new_app)
    return urls

class Command(BaseCommand):
    help = "Display all URL patterns with app source"

    def handle(self, *args, **options):
        resolver = get_resolver()
        urls = list_urls(resolver.url_patterns)
        
        # Filter out admin URLs
        urls = [u for u in urls if not u['url'].startswith('admin/')]

        # Print table header
        print("{:<40} {:<25} {:<15}".format("URL", "Name", "App Source"))
        print("-"*85)
        for u in urls:
            print("{:<40} {:<25} {:<15}".format(u['url'], u['name'], u['app']))
