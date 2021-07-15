import requests
from django.shortcuts import render


# Create your views here.
from django.template import loader


def index(request):
    r = requests.get(
        'https://76be168a551fe81aa7b781bff4221beb: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@teststoreformanasfinal.myshopify.com/admin/api/2021-07/inventory_levels.json?inventory_item_ids=42647108485273/',
        auth=('76be168a551fe81aa7b781bff4221beb', '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'))
    r = r.json()
    r = r['inventory_levels']
    total_inv = 0
    for i in range(len(r)):
        total_inv = total_inv + r[i]['available']
    print(total_inv)
    template = loader.get_template('index.html')
    context = {
        'inventory_avail': total_inv,
    }
    return render(request, 'index.html', {'inventory_avail': total_inv})
