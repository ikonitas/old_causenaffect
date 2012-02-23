from django.shortcuts import get_object_or_404
from blog.models import Entry
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from djpjax import pjax
import datetime
import calendar
from time import strptime
from django.http import Http404

@pjax("pjax/blog_pjax.html")
def blog_index(request):
    entries_list = Entry.objects.all()

    try:
        page = request.GET.get('page',1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(entries_list, 1)
    entries = p.page(page)
    archive = home_archive()
    return TemplateResponse(request,"blog/blog.html",{'entries':entries,
                                                     'archive':archive})
    #return render_to_response("blog/blog.html",{'entries':entries},
    #        context_instance=RequestContext(request))

def home_archive():
    events = Entry.objects.all()
    year_now = datetime.datetime.now().year
    data = []
    for event in events:
        if year_now == event.pub_date.year:
            data.append(event)
    data = {year_now:[calendar.month_abbr[p] for p in sorted(set(d.pub_date.month for d in data))]}
    return data


@pjax("pjax/blog_detail_pjax.html")
def entries_detail(request, slug):
    blog = get_object_or_404(Entry, slug=slug)
    archive = home_archive()
    return TemplateResponse(request, "blog/blog_detail.html",{"blog":blog, 'archive':archive})
    #return render_to_response("events/event_detail.html", {'event':event},
    #        context_instance=RequestContext(request))





@pjax("pjax/blog_year_pjax.html")
def entries_year(request, year):
    year = int(year)
    whole_years = []
    for event in Entry.objects.all():
        if event.pub_date.year not in whole_years:
            whole_years.append(event.pub_date.year)
    if year not in whole_years:
        raise Http404
    blogs = Entry.objects.filter(pub_date__year=year)
    archive = home_archive()

    return TemplateResponse(request, "blog/archive/blog_year.html",{'blogs':blogs,'year':year,'archive':archive})
    #return render_to_response("blog/archive/entries_year.html",{'events_year':entries_year, 'year':year,}, context_instance=RequestContext(request))



@pjax("pjax/blog_months_pjax.html")
def entries_months(request, year, month):
    year = int(year)

    month = strptime(month,'%b').tm_mon

    whole_years = []
    whole_months = []
    for event in Entry.objects.all():
        if event.pub_date.year not in whole_years:
            whole_years.append(event.pub_date.year)
        if event.pub_date.month not in whole_months:
            whole_months.append(event.pub_date.month)

    if month not in whole_months:
        raise Http404
    elif year not in whole_years:
        raise Http404
    archive = home_archive()

    blog_months = Entry.objects.filter(pub_date__year=year, pub_date__month=month)
    return TemplateResponse(request, "blog/archive/blog_months.html",{'events_months':blog_months,'month':month,'year':year,'archive':archive,})
    #return render_to_response("events/archive/events_months.html",{'events_months':events_months,
    #    'month':month, 'year':year}, context_instance=RequestContext(request)) 




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


@pjax("pjax/blog_whole_archive_pjax.html")
def very_archive(request):
    query = Entry.objects.all().order_by('-pub_date')
    object_years_dict = create_archive_list(query)
    archive = home_archive()
    
    return TemplateResponse(request,"blog/archive/blog_whole_archive.html",{'archive_list':object_years_dict,'archive':archive,},)
    #return render_to_response('blog/whole_archive.html', {'archive_list': object_years_dict},
    #    context_instance=RequestContext(request))
