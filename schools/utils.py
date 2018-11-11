import random
import string
from django.utils.text import slugify


DONT_USE=['create']
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        url_endpoint = new_slug
    else:
        url_endpoint = slugify(instance.short_name)
    if url_endpoint in DONT_USE:
        new_slug = "{url_endpoint}-{randstr}".format(
                    url_endpoint=url_endpoint,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(url_endpoint=url_endpoint).exists()
    if qs_exists:
        new_slug = "{url_endpoint}-{randstr}".format(
                    url_endpoint=url_endpoint,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return url_endpoint