# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse

import urllib2
import json





# def home(request):
#     """Renders the home page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/index.html',
#         context_instance = RequestContext(request,
#         {
#             'title':'Home Page',
#             'year':datetime.now().year,
#         })
#     )
#
# def contact(request):
#     """Renders the contact page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/contact.html',
#         context_instance = RequestContext(request,
#         {
#             'title':'Contact',
#             'message':'Your contact page.',
#             'year':datetime.now().year,
#         })
#     )
#
# def about(request):
#     """Renders the about page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/about.html',
#         context_instance = RequestContext(request,
#         {
#             'title':'About',
#             'message':'Your application description page.',
#             'year':datetime.now().year,
#         })
#     )

def index(request):

    return render(request, 'index.html')



def search(request):
    print 'd'
    url = 'https://ussouthcentral.services.azureml.net/workspaces/753da512f5944a489994fd9b63885c50/services/a9b9f699df7d434e9e07b71ce321da62/execute?api-version=2.0&details=true'
    api_key = 'oXpIAqhmlx7f84EbmX/zGvnj+lOYE01Ma68cbzaqb9bStV3TDDxgh+q5j4OX5NPDfPV0H5lS6fOCeWwMkeQs5Q=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}
    data = {
        "Inputs": {
            "input1": {
                "ColumnNames": [
                    "symboling",
                    "normalized-losses",
                    "make",
                    "fuel-type",
                    "aspiration",
                    "num-of-doors",
                    "body-style",
                    "drive-wheels",
                    "engine-location",
                    "wheel-base",
                    "length",
                    "width",
                    "height",
                    "curb-weight",
                    "engine-type",
                    "num-of-cylinders",
                    "engine-size",
                    "fuel-system",
                    "bore",
                    "stroke",
                    "compression-ratio",
                    "horsepower",
                    "peak-rpm",
                    "city-mpg",
                    "highway-mpg",
                    "price"
                ],
                "Values": [
                    [
                        request.GET.get("symboling","2"),
                        request.GET.get("normalized-losses","164"),
                        request.GET.get("make","audi"),
                        request.GET.get("fuel-type","gas"),
                        request.GET.get("aspiration","std"),
                        request.GET.get("num-of-doors","four"),
                        request.GET.get("body-style","sedan"),
                        request.GET.get("drive-wheels","fwd"),
                        request.GET.get("engine-location","front"),
                        request.GET.get("wheel-base","99.8"),
                        request.GET.get("length","176.6"),
                        request.GET.get("width","66.2"),
                        request.GET.get("height","54.3"),
                        request.GET.get("curb-weight","2337"),
                        request.GET.get("engine-type","ohc"),
                        request.GET.get("num-of-cylinders","four"),
                        request.GET.get("engine-size","109"),
                        request.GET.get("fuel-system","mpfi"),
                        request.GET.get("bore","3.19"),
                        request.GET.get("stroke","3.4"),
                        request.GET.get("compression-ratio","10"),
                        request.GET.get("horsepower","102"),
                        request.GET.get("peak-rpm","5500"),
                        request.GET.get("city-mpg","24"),
                        request.GET.get("highway-mpg","30"),
                        request.GET.get("price","0"),
                    ],

                ]
            }
        },
        "GlobalParameters": {}
    }
    body = str.encode(json.dumps(data))
    print body
    req = urllib2.Request(url, body, headers)
    dict = {'error':'1'}
    try:
        response = urllib2.urlopen(req)
        result = response.read()
        price = json.loads(result)
        price = price["Results"]
        price = price["output1"]
        price = price["value"]
        price = price["Values"]
        price = price[0]
        price = price[-1]
        print price
        dict = {'price': price}

    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
        print(json.loads(error.read()))
    return JsonResponse(dict)
