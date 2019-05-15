from django.shortcuts import render

# Create your views here.
import random
import json


def index(request):
    names = ("bob", "dan", "jack", "lizzy", "susan")

    items = []
    for i in range(100):
        items.append({
            "name": random.choice(names),
            "age": random.randint(20,80),
            "url": "https://example.com",
        })

    #context = {}
    #context["items"] = items
    context = {}
    context["items_json"] = json.dumps(items)
    return render(request, 'simple_vuejs/vue_list.html', context)



