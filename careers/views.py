
# Updated Code
from django.shortcuts import render
from django.http import JsonResponse
from .models import CareerPath, Role


def dendrogram(request):
    return render(request, 'careers/dendrogram.html')


def career_paths_data(request):
    career_paths = CareerPath.objects.all()
    data = {
        'name': 'Career Paths',
        'children': [
            {
                'name': career.title,
                'children': [
                    {'name': role.title} for role in Role.objects.filter(career_path=career)
                ]
            }
            for career in career_paths
        ]
    }
    return JsonResponse(data)

def career_paths_api(request):
    data = list(CareerPath.objects.values('id', 'name', 'parent_id'))
    return JsonResponse(data, safe=False)

