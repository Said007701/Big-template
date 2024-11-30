from rest_framework import serializers
from . import models

class HeaderTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeaderTop
        fields = '__all__'
        
class HeaderCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeaderCenter
        fields = '__all__'
class HeaderEndSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeaderEnd
        fields = '__all__'
class HeaderSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeaderSlider
        fields = '__all__'
        
        
class MainOneTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainOneTop
        fields = '__all__'
        
class MainOneLeftSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainOneLeft
        fields = '__all__'
class MainOneRightSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainOneRight
        fields = '__all__'

class MainTwoLeftSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainTwoLeft
        fields = '__all__'
        
class MainTwoRightSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainTwoRight
        fields = '__all__'
        

class MainTheeTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainTheeTop
        fields = '__all__'
        
class MainTheeContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainTheeContent
        fields = '__all__'
        

class MainFourTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainFourTop
        fields = '__all__'
        
class MainFourLeftSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainFourLeft
        fields = '__all__'
class MainFourRightSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainFourRight
        fields = '__all__'
        
# Footer Start
class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Footer
        fields = '__all__'