
# Updated Code
from django.http import JsonResponse
from .models import CareerPath

def career_paths_api(request):
    try:
        # Get a list of dictionaries representing CareerPath objects
        data = list(CareerPath.objects.values('id', 'title', 'description'))
        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})
    except Exception as e:
        # Log the error and return an appropriate response
        # Optionally, use logging here
        return JsonResponse({'error': str(e)}, status=500)

