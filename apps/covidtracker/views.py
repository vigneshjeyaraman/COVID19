from io import BytesIO
import base64
from datetime import datetime
from covid import Covid
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use("Agg")

from django.shortcuts import render


# Create your views here.
covid = Covid()
def home(request):
    data = covid.get_data()
    last_updated = datetime.utcfromtimestamp(data[0]['last_update']/1000).strftime('%Y-%m-%d %H:%M:%S')
    countries = [x['country'] for x in data]
    active = [x['active'] for x in data]
    plt.xlabel('Country')
    plt.ylabel('Active cases')
    plt.title('Covid active cases in top 15 countries')
    plt.bar(countries[:15], active[:15])
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.xticks(rotation=90)
    plt.tight_layout() 
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()
    return render(request, 'home.html', {"image_base64": image_base64, "last_updated": last_updated})

def searchcountry(request):
    countries = covid.list_countries()
    if request.method == 'POST':
        country_stats = covid.get_status_by_country_id(request.POST.get('country'))
        last_updated = datetime.utcfromtimestamp(country_stats['last_update']/1000).strftime('%Y-%m-%d %H:%M:%S')
        return render(request, 'searchforyourcountry.html', {'countries': countries, "stats": country_stats, "selected": country_stats['country'], "last_updated": last_updated})
    return render(request, 'searchforyourcountry.html', {'countries': countries})

def overview(request):
    active = covid.get_total_active_cases()
    confirmed = covid.get_total_confirmed_cases()
    recovered = covid.get_total_recovered()
    deaths = covid.get_total_deaths()
    return render(request, "overview.html", {"active": active, "confirmed": confirmed, "recovered": recovered, "death": deaths})