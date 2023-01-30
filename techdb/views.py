from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import datetime

from .models import (Site, Category, SiteCommon, SiteEquipment, SiteBatteries, SiteRRL, SiteEnergy, SiteOldInfo,
                     SiteQuazar, PhoneBook, DutyTimetable)
from .forms import SiteForm, CommentForm


def index(request):
    sites = Site.objects.all()
    paginator = Paginator(sites, 150)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    all_dutys = DutyTimetable.objects.all()
    now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for i in all_dutys:
        if str(i.date_start) < str(now_date) and str(i.date_end) > str(now_date):
            today_duty = i
    return render(request, 'techdb/index.html', {'page': page, 'today_duty': today_duty})


def by_category(request, category_id):
    sites = Site.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'sites': sites, 'categories': categories, 'current_category': current_category}
    return render(request, 'techdb/by_category.html', context)


def site_view(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    site_common = SiteCommon.objects.get(title_id=site_id)
    site_equipment = SiteEquipment.objects.filter(title_id=site_id)
    site_rrl = SiteRRL.objects.filter(title_id=site_id)
    site_energy = SiteEnergy.objects.filter(title_id=site_id)
    site_old_info = SiteOldInfo.objects.filter(title_id=site_id)
    site_batteries = SiteBatteries.objects.get(title_id=site_id)
    site_quazar = SiteQuazar.objects.filter(title_id=site_id)
    comments = site.comment.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.site = site
            new_comment.author = request.user.get_full_name()
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, "techdb/site.html", {'site': site, 'site_common': site_common,
                                                'site_equipment': site_equipment,
                                                'site_batteries': site_batteries,
                                                'site_rrl': site_rrl,
                                                'site_energy': site_energy,
                                                'site_old_info': site_old_info,
                                                'comments': comments,
                                                'comment_form': comment_form,
                                                'site_quazar': site_quazar})


class SearchResultsView(ListView):
    model = Site
    template_name = 'techdb/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Site.objects.filter(
            Q(title__icontains=query) | Q(address__icontains=query)
        )
        return object_list


@login_required
def new_site(request):
    form = SiteForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'techdb/new.html', {'form': form})
    new_site = form.save(commit=False)
    new_site.save()
    return redirect('index')


def bss_info(request):
    return render(request, 'techdb/bss_info.html')
    

def tn_info(request):
    return render(request, 'techdb/tn_info.html')


def phonebook(request):
    phones = PhoneBook.objects.all()
    return render(request, 'techdb/phonebook.html', {'phones': phones})


def useful_sites(request):
    return render(request, 'techdb/useful_sites.html')


def shedule(request):
    now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dutys = DutyTimetable.objects.filter(date_start__gt=str(now_date))    
    dutys_past = DutyTimetable.objects.filter(date_start__lt=str(now_date))[74:]
    # duty_today = DutyTimetable.objects.filter(date_start__lt=str(now_date), date_end__gt=str(now_date))
    return render(request, 'techdb/shedule.html', {'dutys': dutys, 'dutys_past': dutys_past})
    