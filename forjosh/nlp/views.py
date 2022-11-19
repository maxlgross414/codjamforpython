from django.shortcuts import render

from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####
import requests

API_URL = "https://api-inference.huggingface.co/models/yanekyuk/bert-uncased-keyword-extractor"
headers = {"Authorization": "Bearer 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"}

def get_key(input):
    print(input)


    topic = input.GET.get('topic', None)

    print(topic)

    query = {
        'inputs': topic
    }

    print(query)

    output = requests.post(API_URL, headers=headers, json=query)
    
    return JsonResponse(output.json(), safe=False)

def index(input):
    return HttpResponse("Hello, world. You're at the wiki index.")

