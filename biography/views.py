from biography.models import Biography
from djpjax import pjax
from django.template.response import TemplateResponse

@pjax("pjax/biography_pjax.html")
def biography_view(request):
    try:
        biography = Biography.objects.all()[0]
    except IndexError:
        biography = ''

    return TemplateResponse(
        request,
        "biography/biography.html",
        {'biography':biography}
    )
