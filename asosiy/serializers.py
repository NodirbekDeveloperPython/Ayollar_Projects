from rest_framework.serializers import ModelSerializer
from .models import *
class K_BolimSerializer(ModelSerializer):
    class Meta:
        model = Konstitsiya_Bolim
        fields = '__all__'

class K_BobSerializer(ModelSerializer):
    class Meta:
        model = Konstitsiya_Bob
        fields = '__all__'

class K_ModdaSerializer(ModelSerializer):
    class Meta:
        model = Konstitsiya_Modda
        fields = '__all__'

