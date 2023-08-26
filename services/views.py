from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Services
from .serializers import ServicesSerializer

# API TESTED OK ___________________________________________________________
@api_view(['GET', 'POST'])
def services_list(request):
    if request.method == 'GET':
        services = Services.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
# API TESTED OK ___________________________________________________________
    
@api_view(['GET', 'PUT', 'DELETE'])
def services_detail(request, slug):
    try:
        service = Services.objects.get(slug=slug)
    except Services.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ServicesSerializer(service)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServicesSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        service.delete()
        return Response(status=204)