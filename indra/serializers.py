from rest_framework import *
from indra.models import *


class BusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bus
		fields = ('passenger_name','passenger_id','mail_id','age','arrival','destination','phone_number')