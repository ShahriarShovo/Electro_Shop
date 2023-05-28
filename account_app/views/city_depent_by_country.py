from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from account_app.models.drop_down import Countries, Cities


@csrf_protect
def city_dependent_by_country_view(request):
    country_id = request.GET.get('country_id')
    print(country_id)
    city = Cities.objects.filter(country__id=country_id).values('id', 'country', 'city_name')
    data = {
        'city_list': list(city)
    }
    return JsonResponse(data)
