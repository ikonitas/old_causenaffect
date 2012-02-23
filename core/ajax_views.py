from events.models import Event
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from blog.models import Entry
import calendar
import datetime
import itertools

@csrf_exempt
def archive(request):
    post = request.POST['arch[]']
    if post == 'events':
        #response_dict = {"test":"PAVYKO!"}
        #return HttpResponse(simplejson.dumps(response_dict),mimetype="application/javsacript")
        #listas = [p.pub_date for p in Event.objects.all()]
        #data = dict((year, [calendar.month_abbr[m] for m in sorted(set(d.month for d in year_dates))]) for year, year_dates in itertools.groupby(sorted(listas), lambda d: d.year))
        events = Event.objects.all()
        year_now = datetime.datetime.now().year 
        data = []
        for event in events:
            if year_now == event.pub_date.year:
                data.append(event)
        data = {year_now:[calendar.month_abbr[p] for p in sorted(set(d.pub_date.month for d in data))]}
        return HttpResponse(simplejson.dumps(data), mimetype="application/javascript")
    elif post == "blog":
        entries = Entry.objects.all()
        year_now = datetime.datetime.now().year
        data = []
        for blog in entries:
            if year_now == blog.pub_date.year:
                data.append(blog)
        data = {year_now:[calendar.month_abbr[p] for p in sorted(set(d.pub_date.month for d in data))]}
        return HttpResponse(simplejson.dumps(data), mimetype="application/javascript")
    else:
        return HttpResponse(simplejson.dumps({"":""}), content_type="text/plain")
