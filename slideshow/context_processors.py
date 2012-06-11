from slideshow.models import Image

def images(request):
    try:
        images = Image.objects.filter(is_active=True).order_by('?')
    except:
        return {'images':''}

    return {'images': images}
