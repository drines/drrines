from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def quotes(request):
    return render(request, 'quotes.html')

def tdauth(request):
    response = requests.get('https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=dev.drrines.com&client_id=DRRINES001@AMER.OAUTHAP')
    return HttpResponse(request, response)
