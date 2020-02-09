from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, get_object_or_404
from .forms import UrlForm
from .models import Url
from .utils import *
import sys
import random
import string
import re
# Create your views here.
BASE_URL = 'http://127.0.0.1:8000/'
def home(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            new_url = Url()
            long_url = form.data['long_url']
            url_regex = re.compile(r"^(https?:\/\/)?(www\.)?(.+\.\w+.*)")
            long_url = url_regex.sub(r'\3', long_url)

            new_url.long_url = long_url
            to_hash = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(100))
            encoded = encode(hash(to_hash) % ((sys.maxsize + 1) * 2))
            
            new_url.short_url = BASE_URL + str(encoded) 
            
            new_url.long_url_encoded = encoded
            new_url.save()
            context = {
                'generated_url': new_url,
                'generated': True,
                'form': UrlForm()
            }
            return render(request, 'urlshortenservice/home.html', context)
            
    form = UrlForm()
    context = {
        'form': form,
        'generated': False
    }
    return render(request, 'urlshortenservice/home.html', context)


def redirect_to_site(request, encoded_url):
    current_url = get_object_or_404(Url, long_url_encoded = encoded_url)
    if current_url:
        return HttpResponseRedirect("https://" + current_url.long_url)