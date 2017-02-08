from django.shortcuts import render
from rest_framework import status,permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from indra.models import Bus
from indra.serializers import BusSerializer
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def passenger_list(request):
	if request.method == 'GET':
		passenger = Bus.objects.all()
		serializer =BusSerializer(passenger, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = BusSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





