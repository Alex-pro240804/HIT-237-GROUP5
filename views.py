from django.shortcuts import render, get_object_or_404
from mango_app.pest_disease_data import pest_diseases_list
from django.http import Http404

def home(request):
    return render(request, 'mango_app/home_page.html')

def pest_disease_list(request):
    context = {
        'problems': pest_diseases_list
        }
    return render(request, 'mango_app/pest_disease_list.html', context)

def pest_disease_detail(request, issue_name):
    problem = None
    for item in pest_diseases_list:
        if item.name.lower() == issue_name.lower():
            problem = item
            break
    if problem is None:
        raise Http404("Pest/disease not found")
    context = {
        'problem': problem
        }
    return render(request, 'mango_app/pest_disease_detail.html', context)

def about(request):
    team_members = [
        {
            "name": "Alex Shaji", "id": "S374208"
        },
        {
            "name": "Elka Mary Shibu", "id": "S374234"
        },
        {
            "name": "Navaneeth Sreekumar", "id": "S376549"
        },
        {
            "name": "Nahyan Al Masood", "id": "S361022"
        },
    ]
    context = {
        'team_members': team_members
        }
    return render(request, 'mango_app/about_page.html', context)