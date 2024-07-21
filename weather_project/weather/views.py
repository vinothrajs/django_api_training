from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Weather
from .serializers import WeatherSerializer


@api_view(['GET'])
def view_all_weather(request):
    weathers = Weather.objects.all()
    serializer = WeatherSerializer(weathers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_weather(request):
    serializer = WeatherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search_weather(request):
    city = request.GET.get('city', None)
    if city is not None:
        weathers = Weather.objects.filter(city__icontains=city)
        serializer = WeatherSerializer(weathers, many=True)
        return Response(serializer.data)
    return Response({"error": "City parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
