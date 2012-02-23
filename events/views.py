from events.models import Event
from django.shortcuts import get_object_or_404
from events.models import Event
from django.http import Http404
import datetime
from djpjax import pjax
from django.template.response import TemplateResponse
from pure_pagination import Paginator, PageNotAnInteger
from time import strptime
import calendar

@pjax("pjax/events_pjax.html")
def index_view(request):
    
    contact_list = Event.objects.all()

    try:
        page = request.GET.get('page',1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(contact_list, 10)
    events = p.page(page)
    archive = home_archive()

    return TemplateResponse(request, "events/events.html", {'events':events,
                                                            'archive':archive})

def home_archive():
    events = Event.objects.all()
    year_now = datetime.datetime.now().year
    data = []
    for event in events:
        if year_now == event.pub_date.year:
            data.append(event)
    data = {year_now:[calendar.month_abbr[p] for p in sorted(set(d.pub_date.month for d in data))]}
    return data


@pjax("pjax/events_detail_pjax.html")
def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    archive = home_archive()
    return TemplateResponse(request,"events/events_detail.html",{'event':event,'archive':archive})

@pjax("pjax/events_year_pjax.html")
def events_years(request, year):
    year = int(year)
    
    whole_years = []
    for event in Event.objects.all():
        if event.pub_date.year not in whole_years:
            whole_years.append(event.pub_date.year)

    if year not in whole_years:
        raise Http404
    archive = home_archive()
    events_year = Event.objects.filter(event_date__year=year)
    return TemplateResponse(request,"events/archive/events_year.html",{'events_year':events_year,'year':year,'archive':archive})

@pjax("pjax/events_months_pjax.html")
def events_months(request, year, month):
    year = int(year)

    month = strptime(month,'%b').tm_mon

    whole_years = []
    whole_months = []
    for event in Event.objects.all():
        if event.pub_date.year not in whole_years:
            whole_years.append(event.pub_date.year)
        if event.pub_date.month not in whole_months:
            whole_months.append(event.pub_date.month)

    if month not in whole_months:
        raise Http404
    elif year not in whole_years:
        raise Http404
    archive = home_archive()

    events_months = Event.objects.filter(pub_date__year=year, pub_date__month=month)
    return TemplateResponse(request, "events/archive/events_months.html",{'events_months':events_months,'month':month,'year':year,'archive':archive},)


def create_archive_list(_query):
    """
    given a sorted queryset, return a list in the format:
    archive_list = [{'2009': [{'December': ['entry1', 'entry2']},
                              {'January': ['entry3', 'entry4']}
                              ]
                     },
                    {'2008': [{'January': ['entry5', 'entry6']},
                              ]
                     }
                    ]
    """
    archive_list = []
    tmp_months_list = []
    tmp_year_list = []

    for item in _query:
        if item.pub_date.year not in tmp_year_list:
            tmp_year_list.append(item.pub_date.year)
            tmp_dict = {}
            tmp_dict[item.pub_date.year] = []
            archive_list.append(tmp_dict)
        else:
            pass

    for entry in _query:
        for item in archive_list:
            _year = entry.pub_date.year
            if _year in item:
                _tmp_month = entry.pub_date.strftime("%B")
                # make a dictionary with the month name as a key and an empty list as a value
                tmp_dict = {}
                tmp_dict[_tmp_month] = []

                if tmp_dict not in item[_year]:
                    item[_year].append(tmp_dict)
                
                    
    for entry in _query:
        # dict in list
        for item in archive_list:
            # year of entry
            _year = entry.pub_date.year
            if _year in item:
                _year_list = item[_year]
                for _dict_month in _year_list:
                    _tmp_month = entry.pub_date.strftime("%B")
                    if _tmp_month in _dict_month:
                        _dict_month[_tmp_month].append(entry)
                        
    return archive_list

@pjax("pjax/events_whole_archive_pjax.html")
def very_archive(request):
    query = Event.objects.all().order_by('-pub_date')
    object_years_dict = create_archive_list(query)
    archive = home_archive()
    
    return TemplateResponse(request, "events/archive/events_whole_archive.html",{'archive_list':object_years_dict,'archive':archive})
