from slideshow.models import Image

def images(request):
    try:
        images = Image.objects.filter(is_active=True).order_by('?')[:5]
    except:
        return {'images':''}

    return {'images': images}
