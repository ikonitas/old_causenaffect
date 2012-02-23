from photologue.models import Gallery
from djpjax import pjax
from django.template.response import TemplateResponse
from pure_pagination import Paginator, PageNotAnInteger

@pjax("pjax/gallery_pjax.html")
def albums(request):
    galleries = Gallery.objects.all()
    cover = [cover.album_cover.get_thumbnail_url() for cover in galleries]
    try:
        page = request.GET.get('page',1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(galleries, 5)
    galleries = p.page(page)

    return TemplateResponse(request, "gallery/gallery.html",{'galleries':galleries,'cover_image':cover})
